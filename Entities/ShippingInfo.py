class ShippingInfo:
    def __init__(self,from_add,to_add,state):
        self._from_add=from_add
        self._to_add=to_add
        self._state=state
        
    def to_dict(self):
        return {
            "From":self._from_add,
            "To":self._to_add,
            "state":self._state
        }
        