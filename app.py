import os
from requests import post, get
from flask import Flask, request, redirect, url_for, flash, make_response, Response
from flask_cors import CORS
import json
import billing
import auth


app = Flask(__name__)
CORS(app)


@app.route('/<action>/<businessId>', methods=['GET'])
def get_business_data(action, businessId):
    if not auth.check_access(headers=request.headers, businessId=businessId):
      return make_response(json.dumps({'error': 'access not granted'}), 400, {'Content-Type': 'application/json'})

    req = billing.get_action(action, businessId, headers=request.headers, params=request.args)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    
    headers = [(name, value) for (name, value) in req.raw.headers.items() if name.lower() not in excluded_headers]

    response = make_response(req.content, req.status_code, headers)

    print(headers)

    return response

