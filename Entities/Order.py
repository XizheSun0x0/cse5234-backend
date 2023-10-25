class Order:
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
    
    def get_id(self):
        return self._id
    
    def set_id(self,id):
        self._id=id
        
    def get_order(self):
        return self._order
    
    def set_order(self,order):
        self._order=order
        
    
    #jsonify order
    def get_order_json(self,payment_info:dict=None,shipping_info:dict=None):
        return{
            "id":self._id,
            "status":self._status,
            "items":self._items,
            "payment":payment_info,
            "shipping": shipping_info
        }
        