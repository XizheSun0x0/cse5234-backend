from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
#initialize this app
app = Flask(__name__)

CORS(app)