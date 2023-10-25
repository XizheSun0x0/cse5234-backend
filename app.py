from flask import Flask, jsonify, request
from Services.InventoryManagementService import InventoryManagementService
from Services.OrderProcessingService import OrderProcessingService

#initialize this app
app = Flask(__name__)
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
    inventory_json = [item.to_dict() for item in ims.get_available_item()]
    return jsonify(inventory_json)

#return item with certain id and it is available.
@app.route(IM_PATH+"/items/<id>")
def inventory_item_id_api(id):
    target_item=ims.get_available_item_by_id(target_id=id)
    item_json= [item.to_dict() for item in target_item]
    return jsonify(item_json)

#return item with certain name and it is available.
@app.route(IM_PATH+"/items")
def inventory_item_name_api():
    item_name=request.args.get('name')
    target_item=ims.get_available_item_by_name(target_name=item_name)
    item_json=[item.to_dict() for item in target_item]
    return jsonify(item_json)

# test post request.
@app.route("/p",methods = ['POST'])
def respose_to_post():
    data = request.json
    print(type(data))
    dlen = len(data)
    return jsonify(f"Hi, you request with json with len of {dlen}"),200

#process order request
@app.route(OP_PATH+"/order",methods=['POST'])
def response_with_order_api():
    data = request.json
    result=oms.create_pending_order_from_post(data.get("items"),ims)
    if list(result.keys())[0] == 'id':
        return jsonify({"confirmation number":oms.checkout(result,ims)})
    else:
        if list(result.keys())[0] == 'Error':
            return jsonify({"Error":"item not available"})

if __name__=='__main__':
    app.run(port=5001,debug=True)