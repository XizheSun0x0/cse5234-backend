from Entities.Cart import Cart
from Entities.Order import Order
from Entities.SellingItem import SellingItem
from Utility.Utility import IdGenerator as oig
from flask import Flask, jsonify, request
class OrderProcessingService:
    def __init__(self):
        self._orders=[]
    
    #check the avalibility of items from cart
    def check_items_avaibility(self,data,ims):
        res=True
        for item in data:
            if(int(ims.get_availablity_by_id(item.get("id")))<=0):
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
    def checkout(self, order,ims):
        self._orders.append(order)
        ims.update_by_order(order)
        return order.id

    