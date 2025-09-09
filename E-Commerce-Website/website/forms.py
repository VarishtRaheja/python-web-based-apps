# Importing the required libraries
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp, ValidationError
from website.models import User


class RegisterForm(FlaskForm):
    """Flask form for registering new users and subsequent validation

    Args:
        FlaskForm (Inherited class): Flask specific subclass of flask-wtf form
    """
    def validate_username(self,username):
        uname_check = User.query.filter_by(username=username.data).first()
        if uname_check:
            raise ValidationError("Username already exists. Please log in.")
        
    def validate_email_address(self,email_address):
        email_address_check  = User.query.filter_by(email_address=email_address.data).first()
        if email_address_check:
            raise ValidationError("Email already exist. Please try a different address.")
        
    first_name = StringField("First Name",
                             validators=[DataRequired("Field is required."), 
                                         Length(2,12),
                                         Regexp(r"^[a-zA-Z]+$",message="Name must not contain numbers")
                                         ])
    family_name = StringField("Family Name",
                              validators=[DataRequired("Field is required"), 
                                                        Length(2,12),
                                                        Regexp(r"^[a-zA-Z]+$",message="Name must not contain numbers")
                                                        ])
    email_address = EmailField("Email Address",
                               validators=[DataRequired(), 
                                           Length(6,30), 
                                           Email("Please enter a valid email address")
                                           ])
    username = StringField("Username",
                           validators=[DataRequired("Please enter a username of min length 2"), 
                                       Length(2,24)
                                       ])
    password = PasswordField("Password",
                             validators=[DataRequired("Please enter a password of min length 6"), 
                                         Length(6,14)
                                         ])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), 
                                                 Length(6,14), 
                                                 EqualTo("password")
                                                 ])
    
    remember_me = BooleanField("Remember Me",default=False)
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """Login form for signing in existing users into the website to 
    determine authentication of correct user.

    Args:
        FlaskForm (Inherited class): Flask specific subclass of flask-wtf form
    """

    # email = EmailField("Email Address",
    #                    validators=[DataRequired(), Length(6,30), 
    #                                Email("Please enter a valid email address")
    #                                ])
    username = StringField("Username",
                           validators=[DataRequired("Please enter a username of min 2"), 
                                       Length(2,24)
                                       ])
    password = PasswordField("Password",
                             validators=[DataRequired("Please enter a password of min length 6"), 
                                         Length(6,14)
                                         ])
    remember_me = BooleanField("Remember Me",default=False)
    submit = SubmitField("Sign In")
    forgot_password = SubmitField("Forgot Password")
    
    def validate_username(self,username):
        uname_check = User.query.filter_by(username=username.data).first()
        if not uname_check:
            raise ValidationError("Username does not exist. Please try a different username.")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase")  
        
class SellItem(FlaskForm):
    submit = SubmitField(label="Sell")
