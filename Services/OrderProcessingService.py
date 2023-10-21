from Entities.Cart import Cart
from Entities.Order import Order
from Entities.SellingItem import SellingItem
from Utility.Utility import IdGenerator as oig
from flask import Flask, jsonify, request
class OrderProcessingService:
    def __init__(self):
        self._orders=[]
        self._status='True'
    
    #check the avalibility of items from cart
    def check_items_avaibility(self,data,ims):
        res=True
        for idx in range(len(data)):
            current_availablity = int(ims.get_availablity_by_id(data[idx].get("id")))
            required_quantity = int(data[idx]['quantity'])
            if(current_availablity <= 0 or current_availablity < required_quantity):
                res = False
                break
        return res
    
    def get_shipping_info(self):
        return {}
    
    def get_payment_info(self):
        return {}
    
    #generate pending order form POST json.
    def create_pending_order_from_post(self,data,ims):
        if(self.check_items_avaibility(data,ims)):
            oid=oig().generate_id()
            order = Order(oid,data,self.get_payment_info,self.get_shipping_info)
            order_json = order.get_order_json()
            return order_json
        else:
            return {"Error":[{"ID":"1001","description":"exceed item availablity"}]}
        
    #checkout, generate an order and return a confirmation number or Error code.
    def checkout(self, order:dict,ims):
        self._orders.append(order)
        ims.update_quantity_by_order(order)
        order['status']='confirmed'
        return order['id']

    