class Inventory:
    def __init__(self):
        self._items = []
        self._status = 'True'
    
    # CREATE: Adds a new item to the inventory
    def add_item(self, item):
        self._items.append(item)

    # READ: Returns all items in the inventory
    def get_items(self):
        return self._items
    

    # DELETE: Removes an item based on its index
    def delete_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]
            return True
        return False
        
        