from requests import get
from config import CONFIG as config

AUTH_API = config['AUTH_API']


def check_access(headers, businessId = None):
  url = AUTH_API['URL'] + 'business/' + businessId
  print(url, headers)

  res = get(url, headers=headers, timeout=3)
  j = res.json()
  print(j)
  return j['access'] == True


    