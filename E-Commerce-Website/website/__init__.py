# Importing basic packages for usage.
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()               # <-- create the extension instance
b_encrypt = Bcrypt()            # <-- create the extension instance
login_manager = LoginManager()     # <-- create the extension instance

# Create the web application
def create_app():
    """
    Creating a config file to connect to a sqllite database. 
    Using pathlib instead of the conventional os library to construct a file path for your database.db database file.

    Args:
        None
        
    Returns:
        flask app
    """
    main_app = Flask(__name__)
    main_app.config.from_object(Config)
    
    # This is nescessary to link the instances to the flask app.
    db.init_app(main_app)
    b_encrypt.init_app(main_app)
    login_manager.init_app(main_app)
    login_manager.login_view = "views.login_page"
    login_manager.login_message_category = "info"
    
    from .views import views
    main_app.register_blueprint(views,url_prefix="/")
    
    from .auth import auth
    main_app.register_blueprint(auth,url_prefix="/")
    
    return main_app