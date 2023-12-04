from . import db
from sqlalchemy import JSON
class Order(db.Model):
    __tablename__ = 'Order'
    
    id = db.Column(db.String(50), primary_key=True)
    items = db.Column(JSON, nullable=False)
    payment_id = db.Column(db.String(50),db.ForeignKey('Payment.id'))
    shipment_id = db.Column(db.String(50),db.ForeignKey('Shipment.id'))
    
        #empty constructor
    def __init__(self):
        pass
    
    def __init__(self, id, selected_items, payment_info=None, shipping_info=None):
        self._id = id
        self._items = selected_items
        if isinstance(selected_items, list):
            self._status = "pending"
        elif isinstance(selected_items, dict):
            self._status = "confirmed"
        else:
            raise ValueError("selected_items must be of type list or dict")
        self._payment_info = payment_info
        self._shipping_info = shipping_info
    
    #jsonify order
    def get_order_json(self,payment_info:dict=None,shipping_info:dict=None):
        return{
            "id":self._id,
            "status":self._status,
            "items":self._items,
            "payment":payment_info,
            "shipping": shipping_info
        }
    
    def __repr__(self):
        return '<Order %r>' % self.id