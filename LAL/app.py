from shared.shared import app,jsonify,request
from Services.InventoryManagementService import InventoryManagementService
from Services.OrderProcessingService import OrderProcessingService
from LAL.crud import initialize_db
# from .privacy import mysqlpw,db_endpoint

# configure the mysql database, relative to the app instance folder
# test locally to avoid aws charge.
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///lal.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:' + mysqlpw + db_endpoint
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warning
app.config["SQLALCHEMY_ECHO"] = True

#init app with db and load some dummy data
initialize_db(app)

#initilize inventory management service
ims = InventoryManagementService()
# load demo data to inventory management
ims.load_demo_items()

oms=OrderProcessingService()


IM_PATH="/inventory-managment/inventory"
OP_PATH="/order-processing"

@app.route("/")
def lal():
    return {"msg":"This is learn and lend"}
    
#home page
@app.route("/home")
def home():
    return  {"msg":"This is home"}

#return the current inventory items.
@app.route(IM_PATH)
def inventory_api():
    inventory_json =  ims.get_available_item()
    return jsonify(inventory_json)

#return item with certain id and it is available.
@app.route(IM_PATH+"/items/<id>")
def inventory_item_id_api(id):
    target_item=ims.get_available_item_by_id(target_id=id)
    item_json=  target_item
    return jsonify(item_json)

#return item with certain name and it is available.
@app.route(IM_PATH+"/items")
def inventory_item_name_api():
    item_name=request.args.get('name')
    target_item=ims.get_available_item_by_name(target_name=item_name)
    item_json=target_item
    return jsonify(item_json)

#process order request
@app.route(OP_PATH+"/order",methods=['POST'])
async def response_with_order_api():
    data = request.json
    result=oms.create_pending_order_from_post(data.get("selected_items"),ims)
    shipping_info = oms.get_shipping_info(data)
    payment_info = oms.get_payment_info(data)
    shipping_response = await oms.invoke_shipment(shipping_info)
    payment_response = await oms.invoke_payment(payment_info)
    if 'id' in result:
        order_id = oms.checkout(result, ims)
        order_response = {'order_confirmation_number': order_id}

        # Merging responses (assuming shipping_response and payment_response are dictionaries)
        combined_response = {**order_response, **shipping_response, **payment_response}
        return jsonify(combined_response)
    elif 'Error' in result:
        return jsonify({"Error": "item not available"})

