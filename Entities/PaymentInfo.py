class PaymenyInfo:
    def __init__(self,cnum,name,vaild,cvv):
        self._card_number = cnum,
        self._holder_name= name,
        self._vaild=vaild,
        self._cvv=cvv
        
    def to_dict(self):
        return{
            "card_number": self._card_number,
            "holder_name":self._holder_name,
            "vaild":self._vaild,
            "cvv":self._cvv
        }