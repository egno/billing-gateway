from requests import get
from config import CONFIG as config

AUTH_API = config['AUTH_API']


def check_access(headers, businessId = None):
  url = AUTH_API['URL'] + 'business/' + businessId

  res = get(url, headers={'Authorization': headers['Authorization']}, timeout=3)
  j = res.json()
  print(j)
  
  return j['access'] == True


    