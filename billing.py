from requests import get
from config import CONFIG as config

BILLING_API = config['BILLING_API']

def get_action(action, businessId, headers, params):
    url = BILLING_API['URL'] + action
    request_params = dict(params)
    request_params['business'] = 'eq.'+businessId
    req = get(url, params=request_params, timeout=10)
    j = req.json()
    print(j)
    return j    
