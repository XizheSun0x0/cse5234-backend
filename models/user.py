from . import db
class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    item_id = db.Column(db.SmallInteger, db.ForeignKey('Item.id'))
    
    def __init__(self,id,name,item_id):
        self.id=id
        self.name=name
        self.item_id=item_id
        
    def __repr__(self):
        return '<User %r>' % self.id