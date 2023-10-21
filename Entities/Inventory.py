class Inventory:
    def __init__(self):
        self._items = []
    
    # CREATE: Adds a new item to the inventory
    def add_item(self, item):
        self._items.append(item)

    # READ: Returns all items in the inventory
    def get_items(self):
        return self._items
    
    def get_item_idx (self,item):
        idx=len(self.get_items)-1
        while(idx>-1):
            if item.get_id() == self._items[idx]:
                break
            idx = idx -1
        return idx

    # UPDATE: Updates an item based on its index
    def update_item(self, index, new_item):
        if 0 <= index < len(self._items):
            self._items[index] = new_item
            return True
        return False

    # DELETE: Removes an item based on its index
    def delete_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]
            return True
        return False
        
        