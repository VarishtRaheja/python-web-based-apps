# Importing file-specific packages
from . import db
from .views import Product

#Importing libraries
import requests
from random import randrange
import logging


def product_information():
    """Function to generate fake commerce data and assign them to the required columns in db.Model

    Args:
        n (int, optional): This API has a limit of ~20 requests since its free 
        so the default has been set to 20.
        
    Returns:
        None
        Commits product information to the database columns as rows.
    """
    db.drop_all()
    db.create_all()
    products = []
    
    try:
        data = "https://fakestoreapi.com/products"
        resp = requests.get(data, timeout=6)
        resp.raise_for_status()
        product_list = resp.json()
    except requests.exceptions.ConnectionError as e:
        logging.error("Connection failed: {} \n Status Code: {}".format(e,resp.status_code))
    except requests.exceptions.Timeout:
        logging.error("Request timed out!")
    finally:    
        for items in product_list:
            products.append(Product(
                name=items["title"],
                barcode=str(randrange(10**11,10**12)),
                description=items["description"],
                price=items["price"],
                img_url=items["image"]
            ))
    
    db.session.bulk_save_objects(products)
    db.session.commit()