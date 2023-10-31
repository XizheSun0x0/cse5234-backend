from __init__ import db
class Order(db.Model):
    __tablename__ = 'Order'
    
    Order_N = db.Column(db.SmallInteger, primary_key=True)
    Item_N = db.Column(db.SmallInteger)
    Sell_Email = db.Column(db.String(50), db.ForeignKey('User.Email'))
    Buy_Email = db.Column(db.String(50), db.ForeignKey('User.Email'))
    Lend_To = db.Column(db.DateTime)