#Importing required libraries
from datetime import datetime
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask import Blueprint, render_template, redirect, url_for, flash, request
from random import randint

# Importing internal file specific modules
from . import db
from website.forms import LoginForm, RegisterForm, PurchaseItemForm, SellItem
from website.models import Product, User, PurchaseHistory



# Creating a blueprint class and the respective routes here.
views = Blueprint("views",__name__)

# Home page 
@views.route("/")
@views.route("/home")
def index():
    # Indexing some products to show random few on home page.
    PRODUCTS = Product.query.all()[randint(2,4):randint(5,8)]
    return render_template("home.html",categories=PRODUCTS)

# Market page
@views.route("/market",methods=["GET","POST"])
@login_required
def marketplace():
    purchase_form = PurchaseItemForm()
    sell_form = SellItem()
    if request.method=="POST" and purchase_form.validate_on_submit():
        purchased_item_id = request.form.get("purchased_item_id")
        # Check if item exists
        p_item_obj = Product.query.filter_by(id=purchased_item_id).first()
        # Check if name exists
        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
                purchase_entry = PurchaseHistory(
                    user_id=current_user.id,
                    product_id=p_item_obj.id,
                    name=p_item_obj.name,
                    price=p_item_obj.price,
                )
                current_user.initial_budget -= p_item_obj.price
                db.session.add(purchase_entry)
                db.session.commit()
                flash(f"Product {p_item_obj.name} was successfully purchased!",category="info")
                return redirect(url_for("views.marketplace"))
            else:
                flash(f"Product, {p_item_obj.name}, purchase has failed. Insufficient funds.",category="error")
    # Creating the link between the product and purchase id
    # Assuming purchase__history.product_id == Product.id
    # owned_items = Product.query.join(
    #     PurchaseHistory,PurchaseHistory.product_id == Product.id
    #     ).filter(
    #         PurchaseHistory.user_id == current_user.id
    #         ).all()
    if sell_form.validate_on_submit():
        p_item_obj = Product.query.filter_by(id=purchased_item_id).first()
        current_user.initial_budget += p_item_obj.price
        
    if request.method=="GET":
        # Using the backref to query the products from purchase history.
        purchases = current_user.cart_items
        item_list = Product.query.filter_by(owner=None).all()
        return render_template("market.html",item_order=item_list, purchase_form=purchase_form,owned_items=purchases,sell_form=sell_form)

# Login page
@views.route("/login",methods=["GET","POST"])
def login_page():
    login_form = LoginForm()
    if request.method == "POST" and login_form.validate_on_submit():
        # uname = request.form["username"]
    # Login and user verification check
        attempted_username = User.query.filter_by(username=login_form.username.data).first()
        if attempted_username and attempted_username.check_password(plaintext=login_form.password.data):
            if login_user(attempted_username,remember=login_form.remember_me.data,force=True):
                flash("Logged in Successfully. User {}, welcome".format(attempted_username.username),category="success")
                return redirect(url_for("views.marketplace"),code=302)
        else:
            flash('Invalid credentials. If new here, please register first.',category="danger")
            return redirect(url_for("views.login_page"),code=302)

    return render_template("login.html",form=login_form)

# Register page
@views.route("/register",methods=["GET","POST"])
def register_page():
    forms = RegisterForm()
    #The method does the form processing work
    if forms.validate_on_submit():
        # Adding to the user class database
        user_to_create = User(first_name=forms.first_name.data,
                              family_name=forms.family_name.data,
                              username=forms.username.data,
                              email_address=forms.email_address.data,
                              password=forms.password.data,
                              )

        # Adding the user to the database called users.
        db.session.add(user_to_create)
        db.session.commit()
        
        if not user_to_create.is_authenticated:
            flash("You need to be logged in to view the products.",category="warning")
            return redirect(url_for("views.login_page"))
        # Creating a message to display when validating the registeration is successful. 
        login_user(user_to_create)
        flash(f"Hello, {user_to_create.first_name} your account has been registered. Please login to continue.",category="success")
        return redirect(url_for("views.login_page"),code=302)
    
    # If there are no errors from validations
    if forms.errors!={}:
        for err_msg in forms.errors.values():
            flash("There was an error in creating a user {}".format(err_msg),category="danger")
    # Rendering the html page
    return render_template("register.html",form=forms)

# Logout function - redirecting to home page
@views.route("/logout",methods=["GET"])
@login_required
def logout_page():
    # Logout user, authentication is done using the deorator above.
    logout_user()
    flash(f"User {request.form["username"]} has been successfully logged out.",category="success")
    return redirect(url_for("views.index"))