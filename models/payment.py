from . import db

class Payment(db.Model):
    __tablename__ = 'Payment'
    
    Email = db.Column(db.String(50), primary_key=True)
    Card_N = db.Column(db.String(30), unique=True)
    Full_Name = db.Column(db.String(80))
    CVV = db.Column(db.SmallInteger)
    Exp_Date = db.Column(db.SmallInteger)
    
    def __init__(self,email,card_n,full_name,cvv,exp):
        self.Email=email
        self.Card_N=card_n
        self.Full_Name=full_name
        self.CVV=cvv
        self.Exp_Date=exp
        
    def __repr__(self):
        return '<Payment %r>' % self.id