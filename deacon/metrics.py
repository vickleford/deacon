import json
import requests

from auth import token, endpoint

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

def list_metrics(entity_id, check_id):
    
    url = '{ep}/entities/{eid}/checks/{cid}/metrics'.format(ep=endpoint, eid=entity_id, cid=check_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    
    
def fetch_points(entity_id, check_id, metric_name):
    
    url = '{ep}/entities/{eid}/checks/{cid}/metrics/{mn}/plot'