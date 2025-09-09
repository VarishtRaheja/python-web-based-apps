from website import create_app, db
from website.fake_product_info import product_information

main_app = create_app()
with main_app.app_context():
    db.create_all()
    product_information()

if __name__=="__main__":
    main_app.run(debug=True) 