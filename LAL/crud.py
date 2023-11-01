from models import db
from models.item import Item
from models.order import Order
from models.payment import Payment
from models.user import User

# initialize database and then connect it with flask app 
def initialize_db(app):
    db.init_app(app)
    with app.app_context():
        db.drop_all()    # Drop all tables
        db.create_all()
        new_item = Item(11,'football',2,3.99)
        db.session.add(new_item)
        db.session.commit()

#create new item and add into database
def create_item(app,id,name,quantity,price):
    with app.app_context():
        new_item = Item(id,name,quantity,price)
        db.session.add(new_item)
        db.session.commit()
        
#create new order and add into database
def create_order(app,id,item_id,sell,buy):
    with app.app_context():
        new_order = Order(id,item_id,sell,buy)
        db.session.add(new_order)
        db.session.commit()
        
#create new payment and add into database
def create_payment(app,email,card_n,full_name,cvv,exp):
    with app.app_context():
        new_payment = Order(id,email,card_n,full_name,cvv,exp)
        db.session.add(new_payment)
        db.session.commit()
    
#create new user and add into database
def create_user(app,id,name,item_id):
    with app.app_context():
        new_user = User(id,name,item_id)
        db.session.add(new_user)
        db.session.commit()

#read all items from database
def read_all_item(app):
    with app.app_context():
        items = Item.query.all()
        db.session.commit()
        return items
    
#read item from database
def read_item(app,id):
    with app.app_context():
        item = Item.query.get(id)
        if item is not None:
            return item

#read all order from database
def read_all_order(app):
    with app.app_context():
        orders = Order.query.all()
        if orders is not None:
            return orders
        
#read order from database
def read_order(app,id):
    with app.app_context():
        order = Order.query.get(id)
        if order is not None:
            return order
        
#read all payments from database
def read_all_payment(app):
    with app.app_context():
        payments = Payment.query.all()
        if payments is not None:
            return payments
        
#read payment from database
def read_payment(app,email):
    with app.app_context():
        payment = Order.query.get(email)
        if payment is not None:
            return payment
        
#read all user from database
def read_all_user(app):
    with app.app_context():
        users = User.query.all()
        if users is not None:
            return users
        
#read users from database
def read_user(app,id):
    with app.app_context():
        user = Order.query.get(id)
        if user is not None:
            return user

# delete item
def delete_item(app,id):
    with app.app_context():
        item = Item.query.get(id)
        if item is not None:
            db.session.delete(item)
            db.session.commit()
            
# delete order
def delete_order(app,id):
    with app.app_context():
        order = Order.query.get(id)
        if order is not None:
            db.session.delete(order)
            db.session.commit()
            
# delete payment
def delete_item(app,email):
    with app.app_context():
        payment = Payment.query.get(email)
        if payment is not None:
            db.session.delete(payment)
            db.session.commit()

# delete user
def delete_user(app,id):
    with app.app_context():
        user = User.query.get(id)
        if user is not None:
            db.session.delete(user)
            db.session.commit()

# TODO implement update after back and front end combination.
        