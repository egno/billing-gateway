from requests import get
from config import CONFIG as config

BILLING_API = config['BILLING_API']

def get_balance(businessId):
    url = BILLING_API['URL'] + 'business_balance?account=eq.business&business=eq.' + businessId
    req = get(url, timeout=3)
    j = req.json()
    print(j)
    return j