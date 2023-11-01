from . import db

class Item(db.Model):
    __tablename__ = 'Item'
    
    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(50))
    quantity = db.Column(db.SmallInteger)
    price = db.Column(db.Float())
    
    def __init__(self,id,name,quantity,price):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
    
    def __repr__(self):
        return '<Item %r>' % self.id