import os
from pathlib import Path

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "i-shall-make-you-mine"
    # Gettign the absolute path of the dir and saveing the database file.
    base_dir = Path(__file__).parent
    db_file = base_dir/"products.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_file}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False