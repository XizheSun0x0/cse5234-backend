from . import db
from sqlalchemy import JSON
class Order(db.Model):
    __tablename__ = 'Order'
    
    id = db.Column(db.String(50), primary_key=True)
    items = db.Column(JSON, nullable=False)
    payment_id = db.Column(db.String(50),db.ForeignKey('Payment.id'))
    shipment_id = db.Column(db.String(50),db.ForeignKey('Shipment.id'))
    
    def __init__(self, items, payment, shipment):
        self.items = items
        self.payment = payment
        self.shipment = shipment
    
    def __repr__(self):
        return '<Order %r>' % self.id