from . import db

class Payment(db.Model):
    __tablename__ = 'Payment'
    id = db.Column(db.String(50),primary_key=True)
    Card_N = db.Column(db.String(30), unique=True)
    Full_Name = db.Column(db.String(80))
    CVV = db.Column(db.SmallInteger)
    Exp_Date = db.Column(db.String(30))
    
    def __init__(self,email,card_n,full_name,cvv,exp):
        self.Email=email
        self.Card_N=card_n
        self.Full_Name=full_name
        self.CVV=cvv
        self.Exp_Date=exp
        
    def __repr__(self):
        return '<Payment %r>' % self.id
    
    def to_dict(self,amount):
        return {
            "business_entity_name": "LAL",
            "business_entity_account": "20230821",
            "amount": str(amount),
            "customer_name": self.Full_Name,
            "credit_card_number": self.Card_N,
            "expiration_date": self.Exp_Date,
            "cvv_code": str(self.CVV)
        }

