from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# Third party end points
payment_url = "https://3o6x7j5m5pqujjkor6u22e7wwe0eieir.lambda-url.us-east-2.on.aws"
payment_endpoint = "/payment-processing/credit-card-processing/payment"
shipment_url = "https://gl2s3honkh7noncsfwft2lrw2u0cuwjc.lambda-url.us-east-2.on.aws"
shipment_init_endpoint = "/shipment-processing/initiation"
shipment_request_endpoint = "/shipment-processing/shipment"

#initialize this app
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "https://main.d16zhsrumswhkr.amplifyapp.com"}})