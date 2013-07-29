import json
import requests

from auth import endpoint, token

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

def get_monitoring_zones():
    url = '{e}/monitoring_zones'.format(e=endpoint)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    

def get_monitoring_zone(zone_id):
    url = '{e}/monitoring_zones/{zid}'.format(e=endpoint, zid=zone_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()