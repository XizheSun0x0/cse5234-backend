from . import db

class Shipment(db.Model):
    __tablename__ = 'Shipment'
    id = db.Column(db.String(50),primary_key=True)
    
    def __init__(self,id):
        self.id=id
    
    def __repr__(self):
        return '<Shipment %r>' % self.id