import os
from requests import post, get
from flask import Flask, request, redirect, url_for, flash, make_response
from flask_cors import CORS
import json
import billing
import auth


app = Flask(__name__)
CORS(app)


@app.route('/<action>/<businessId>', methods=['GET'])
def get_data(action, businessId):
    if not auth.check_access(headers=request.headers, businessId=businessId):
      return make_response(json.dumps({'error': 'access not granted'}), 400, {'Content-Type': 'application/json'})

    res = billing.get_action(action, businessId, headers=request.headers, params=request.args)
    print(res)

    return make_response(json.dumps(res), 200, {'Content-Type': 'application/json'})

