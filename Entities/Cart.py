from .SellingItem import SellingItem as si
class Cart:
    def __init__(self):
        self._cart=[]
    
    #return current client's cart
    def get_cart(self):
        return self._cart
    
    #setter for cart
    def set_cart(self,new_items):
        self._cart=new_items
    
    #create item in cart
    def create_item(self,id,name,quantity,price):
        item = si(id,name,quantity,price)
        self._cart.append(item)
    
    #find item with specific id
    def search_item(self,target_id):
        res = -1
        for index, item in self.get_cart():
            if item.get_id() == target_id:
                res = index
                break
        return res
    
    #update item quanity in cart. If item with id is in cart, update quantity and return true. Otherwise, return false.
    def update_item_quanity(self,item, id, new_quantity):
        item_idx = self.search_item(id)
        if item_idx>-1:
            item.set_quantity(new_quantity)
            return True
        return False
    
    # delete item with specific id.
    def delete_item(self, id):
        item_idx = self.search_item(id)
        if item_idx:
            self._cart.remove(item_idx)
            return True
        return False

    #return a list with all item in dictionary form.
    def to_dict(self):
        return [item.to_dict() for item in self._cart]

    #load demo items into cart
    def load_demo(self):
        demo_item1 = si("111", "Demo Product 1", 5, 9.99)
        demo_item2 = si("112", "Demo Product 2", 3, 19.99)
        self.add_in_cart(demo_item1)
        self.add_in_cart(demo_item2)
        