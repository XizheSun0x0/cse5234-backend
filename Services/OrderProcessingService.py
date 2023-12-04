from models.order import Order
from Utility.Utility import IdGenerator as oig
from shared.shared import payment_url,payment_endpoint,shipment_url,shipment_init_endpoint,shipment_request_endpoint
import httpx
from shared.shared import jsonify
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
    
    def get_shipping_info(self,data):
        return {
            "recipient_name": data['name'],
            "postal_address": data['address_1'] + data['address_2'] 
            + ', ' + data['city'] + ', ' + data['state'] + ', ' + data['zip'],
            "email": "string",
            "number_of_items": len(data['selected_items']),
            "total_weight": 1,
            "total_dimension": "1",
            "business_entity_name": "LAL",
            "entity_account_number": "20230821"
        }
    
    def get_payment_info(self,data):
        return {
            "business_entity_name": "LAL",
            "business_entity_account": "20230821",
            "amount": 10,
            "customer_name": data['name'],
            "credit_card_number": data['credit_card_numer'],
            "expiration_date": data['expir_date'],
            "cvv_code": data['cvvcode']
        }
    
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
    
    # send a post request to the payment processing microservice endpoint return the microservice's response
    async def invoke_payment(self,payment_info):
        async with httpx.AsyncClient() as client:
            response = await client.post(payment_url + payment_endpoint, json=payment_info)
        response.json()
        return response.json()
    
    async def invoke_shipment(self,shipment):
        async with httpx.AsyncClient() as client:
            response_init = await client.post(shipment_url+ shipment_init_endpoint,json={'message':"shipment request"})
            response_init_content = response_init.json()
            if( "message" in response_init_content and response_init_content["message"].startswith("Please")):
                async with httpx.AsyncClient() as client:
                    response = await client.post(shipment_url + shipment_request_endpoint,json=shipment)
        return response.json()
        
    