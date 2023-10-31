from __init__ import db
class Payment(db.Model):
    __tablename__ = 'Payment'
    
    Email = db.Column(db.String(50), primary_key=True)
    Card_N = db.Column(db.String(30), unique=True)
    Full_Name = db.Column(db.String(80))
    CVV = db.Column(db.SmallInteger)
    Exp_Date = db.Column(db.SmallInteger)