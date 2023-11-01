from . import db
class Order(db.Model):
    __tablename__ = 'Order'
    
    id = db.Column(db.SmallInteger, primary_key=True)
    item_id = db.Column(db.SmallInteger)
    Sell_Email = db.Column(db.String(50), db.ForeignKey('User.id'))
    Buy_Email = db.Column(db.String(50), db.ForeignKey('User.id'))
    
    def __init__(self,id,item_id,sell,buy):
        self.id=id
        self.item_id=item_id
        self.Sell_Email=sell
        self.Buy_Email=buy
    
    def __repr__(self):
        return '<Order %r>' % self.id