from models import db
from models.item import Item
from models.order import Order
from models.payment import Payment
from models.user import User

def initialize_db(app):
    db.init_app(app)
    with app.app_context():
        db.drop_all()    # Drop all tables
        db.create_all()
        new_item = Item(11,'football',2,3.99)
        db.session.add(new_item)
        db.session.commit()