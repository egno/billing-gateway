from requests import get
from dotenv import load_dotenv
import os

load_dotenv()

AUTH_API_URL = os.getenv('AUTH_API_URL')

def check_access(headers, businessId = None):
  url = AUTH_API_URL + '/business/' + businessId

  res = get(url, headers={'Authorization': headers['Authorization']}, timeout=3)
  j = res.json()
  print(j)
  
  return j['access'] == True


    