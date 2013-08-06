import json
import requests

from auth import token, endpoint

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

def get_overview(entities=None):
    """Return the overview view for this account
    
    Params can be URI or ID. Up to 100 entities may be individually selected at a time.
    """
    
    url = "{ep}/views/overview".format(ep=endpoint)
    
    if entities is not None:
        qs = {}
        for e in entities:
            qs.update({'ID': e})
    
        r = requests.get(url, headers=headers, params=qs)
    else:
        r = requests.get(url, headers=headers)
        
    return r.json()