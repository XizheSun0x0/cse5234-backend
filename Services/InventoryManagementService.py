from models.item import Item
from Entities.Inventory import Inventory
from LAL.crud import read_all_item
from shared.shared import app
class InventoryManagementService:
    
    def __init__(self):
        self._inventory=Inventory()
        self._status='True'
    
    #load some demo items to this inventory
    def load_demo_items(self):
        data = read_all_item(app)
        self._inventory = data
    
    # return a list contians item objects.
    def get_inventory(self):
        return self._inventory
    
    # return all the available item.
    def get_available_item(self):
        res=[]
        for item in self.get_inventory():
            if(int(item.get('available_quantity'))>0):
                res.append(item)
        return res
    
    # return all the available item with specific name.
    def get_available_item_by_name(self,target_name):
        res=[] 
        for item in self.get_inventory():
            if(target_name==item.get('name') and int(item.get('available_quantity'))>0):
                res.append(item)
        return res
    
    # return all the available item with specific id.
    def get_available_item_by_id(self,target_id):
        res=[]
        for item in self.get_inventory():
            if(target_id==str(item.get('id')) and int(item.get('available_quantity'))>0):
                res.append(item)
        return res       
    
    #return item's availablity by id
    def get_availablity_by_id(self,target_id):
        res = 0
        for item in self.get_inventory():
            if(str(item.get('id'))==target_id):
                res = item.get('available_quantity')
                break
        return res
    
    def get_idx_by_id(self,target_id):
        res = len(self.get_inventory())-1
        while(res>-1):
            if target_id == self.get_inventory()[res].get('id'):
                break
            res = res -1
        return res
    
    # UPDATE: Updates an item based on its index
    def update_item(self, index, new_item):
        if 0 <= index < len(self.get_inventory()):
            self.get_inventory()[index] = new_item
            return True
        return False
    
    def update_quantity_by_order(self,order):
        sold_items=order.get("items")
        for item in sold_items:
            update_id=item.get('id')
            update_idx = self.get_idx_by_id(update_id)
            new_availability=str(int(self.get_availablity_by_id(update_id))-int(item.get('quantity')))
            new_item = Item(update_id,item.get('name'),new_availability,item.get('price'))
            self.update_item(update_idx,new_item)
        return True