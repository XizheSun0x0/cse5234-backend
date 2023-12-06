from serverless_wsgi import handle_request
from run import app  # Import Flask app here

def lambda_handler(event, context):
    return handle_request(app, event, context)