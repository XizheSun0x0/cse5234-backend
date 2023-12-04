from . import db

class Item(db.Model):
    __tablename__ = 'Item'
    
    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(50))
    quantity = db.Column(db.SmallInteger)
    price = db.Column(db.Float())
    owner_id = db.Column(db.String(50), db.ForeignKey('User.id'))  # Make sure the 'user' table name is correct

    def __init__(self, id, name, quantity, price, owner_id):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.owner_id = owner_id
        
    def get_available_quantity(self):
        return self.quantity
    
    def __repr__(self):
        return '<Item %r>' % self.id
    
    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {
            'id': self.get_id(),
            'name': self.name,
            'available_quantity': self.quantity,
            'price': self.price,
        }
