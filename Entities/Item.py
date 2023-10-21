class Item:
    def __init__(self, id, name, available_quantity, price):
        self._id = id
        self._name = name
        self._available_quantity = available_quantity
        self._price = price

    # Setters
    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_available_quantity(self, available_quantity):
        self._available_quantity = available_quantity

    def set_price(self, price):
        self._price = price

    # Getters
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_available_quantity(self):
        return self._available_quantity

    def get_price(self):
        return self._price
    
    #return a dictionary about a item object
    def to_dict(self):
        return{
            'id':self.get_id(),
            'name':self.get_name(),
            'available_quantity':self.get_available_quantity(),
            'price':self.get_price()
        }