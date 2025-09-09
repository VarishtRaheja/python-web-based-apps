# Importing from inherent files
from datetime import datetime
from sqlalchemy import column, func
from website import db
from website import b_encrypt
from website import login_manager

# Importing from external modules
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Creating the database models here.
class User(db.Model, UserMixin):
    """Creating a databse to store username and passwords of different users who register and login

    Args:
        db (SQL based initiliaser class): Inherited class from sql-alchemy module used to create a sqlite database 

    Returns:
        User(_database_class_): Generates a databse with the defined columns and parameters. 
    """
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(30),nullable=False)
    family_name = db.Column(db.String(30),nullable=False)
    username = db.Column(db.String(30),unique=True,nullable=False,index=True)
    email_address = db.Column(db.String(50),unique=True,nullable=False)
    password_hash = db.Column(db.String(60),nullable=False)
    initial_budget = db.Column(db.Float,default=10000.0,nullable=False)
    
    # ← Refer to the **Product** class (capitalized)
    items = db.relationship("Product",backref="owned_user",lazy=True)
    
    
    def __repr__(self):
        return f"<Records of usernames: {self.username}>"
    
    # Creating the proper numbering system
    @property
    def prettier_budget(self):
        if len(str(self.initial_budget))>=4:
            return f"${self.initial_budget:,}"
        else:
            return f"${self.initial_budget}"
        
    # Setting the budget property to be represented with an internation numbering system    
    @prettier_budget.setter
    def budget(self,user_budget):
        self.initial_budget = user_budget
       
    # encryting the password with a hash to be stored in the database as a security measure.    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,basic_string_password):
        self.password_hash = b_encrypt.generate_password_hash(basic_string_password,10).decode(encoding='utf-8',errors="ignore")
    
    # Validation for password check
    def check_password(self,plaintext):
        return b_encrypt.check_password_hash(self.password_hash,plaintext)
    
    # Method to check if budget not exceeding product price.
    def can_purchase(self,item_obejct):
        return self.price >= item_obejct.price
        
class Product(db.Model):
    """
    With the database connection established and the database object created, 
    use the database object to create a database table for products, which is represented by a model — "db.Model"
    a Python class that inherits from a base class Flask-SQLAlchemy provides through the db database instance you created earlier. 
    Args:
        db (SQL based initiliaser class): Inherited class from sql-alchemy module used to create a sqlite database 

    Returns:
        Product(_database_class_): Generates a databse with the defined columns and parameters. 
    """
    __tablename__ = "products"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)
    barcode = db.Column(db.String(12),nullable=False,unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float,nullable=False)
    img_url = db.Column(db.String(256),unique=True)
    
    # foreign key to users.id
    owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def to_dict(self):
        return {column.name: getattr(self,column.name)
                for column in self.__table__.columns}
    
    def __repr__(self):
        return f"<Fake product names: {self.name}>"
    
    
class PurchaseHistory(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)
    price = db.Column(db.Float,nullable=False)
    date = db.Column(db.DateTime,nullable=False,server_default=func.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    user = db.relationship('User', backref='cart_items', lazy=True)
    product = db.relationship('Product', backref='cart_items', lazy=True)