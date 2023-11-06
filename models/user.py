from . import db
class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
    def __repr__(self):
        return '<User %r>' % self.id