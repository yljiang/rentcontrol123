import datetime

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

conn = os.environ.get('MONGODB_URI')
client = MongoClient(conn)
db = client['realEstate']
buildings_collection = db['nycRentControlledBuildings']

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/getRentControlled', methods=['GET'])
@cross_origin()
def get_rent_controlled():
    address = request.args.get('address')
    # Check if the address is rent-controlled
    is_rent_controlled = False
    if buildings_collection.find_one({'address': address}):
        is_rent_controlled = True

    return jsonify({
        'isRentControlled': is_rent_controlled,
        'address': address
    })

@app.route('/about', methods=['GET'])
@cross_origin()
def about():
    address = request.args.get('address')
    # Check if the address is rent-controlled
    is_rent_controlled = False
    if buildings_collection.find_one({'address': address}):
        is_rent_controlled = True

    return jsonify({
        'isRentControlled': is_rent_controlled,
        'address': address
    })