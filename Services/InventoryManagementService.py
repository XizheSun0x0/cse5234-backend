from Entities.Item import Item
from Entities.Inventory import Inventory

class InventoryManagementService:
    
    def __init__(self):
        self._inventory=Inventory()
        self._status='True'
    
    #load some demo items to this inventory
    def load_demo_items(self):
        demo_items = []
        demo_items.append(Item("101", "Golf Balls", "1000", "9.99"))
        demo_items.append(Item("102", "Driver", "500", "99.99"))
        demo_items.append(Item("103", "Club 7", "200", "49.99"))
        demo_items.append(Item("104", "Club 9", "100", "49.99"))
        demo_items.append(Item("201","Calculator","2","10"))
        demo_items.append(Item("202","Ticket: OSU VS UMICH","2","3000"))
        demo_items.append(Item("000","___","0","0"))
        self._inventory = demo_items
    
    # return a list contians item objects.
    def get_inventory(self):
        return self._inventory
    
    # return all the available item.
    def get_available_item(self):
        res=[]
        for item in self.get_inventory():
            if(int(item.get_available_quantity())>0):
                res.append(item)
        return res
    
    # return all the available item with specific name.
    def get_available_item_by_name(self,target_name):
        res=[] 
        for item in self.get_inventory():
            if(target_name==item.get_name() and int(item.get_available_quantity())>0):
                res.append(item)
        return res
    
    # return all the available item with specific id.
    def get_available_item_by_id(self,target_id):
        res=[]
        for item in self.get_inventory():
            if(target_id==item.get_id() and int(item.get_available_quantity())>0):
                res.append(item)
        return res       
    
    #return item's availablity by id
    def get_availablity_by_id(self,target_id):
        res = 0
        for item in self.get_inventory():
            if(item.get_id()==target_id):
                res = item.get_available_quantity()
                break
        return res
    
    def get_idx_by_id(self,target_id):
        res = len(self.get_inventory())-1
        while(res>-1):
            if target_id == self.get_inventory()[res].get_id():
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