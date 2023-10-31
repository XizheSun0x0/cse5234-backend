from __init__ import db
class User(db.Model):
    __tablename__ = 'User'
    
    Email = db.Column(db.String(50), primary_key=True)
    User_Name = db.Column(db.String(50), unique=True)
    Item_N = db.Column(db.SmallInteger, db.ForeignKey('Item.Item_N'))
    Sell_Buy = db.Column(db.String(1))