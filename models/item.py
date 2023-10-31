from __init__ import db
class Item(db.Model):
    __tablename__ = 'Item'
    
    Item_N = db.Column(db.SmallInteger, primary_key=True)
    Item_Name = db.Column(db.String(50))
    Quantity = db.Column(db.SmallInteger)