from requests import get
from dotenv import load_dotenv
import os

load_dotenv()

BILLING_API_URL = os.getenv('BILLING_API_URL')

def get_action(action, businessId, headers, params):
    url = f'{BILLING_API_URL}/{action}'
    request_headers = dict([(name, value) for (name, value) in (dict(headers)).items() if name.lower() not in ['authorization']])
    request_params = dict(params)
    request_params['business'] = 'eq.'+businessId
    print(request_params)
    req = get(url, headers=request_headers, params=request_params, timeout=10)
    print(req.raw.headers)
    return req
