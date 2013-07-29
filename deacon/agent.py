import json
import requests

from auth import token, endpoint

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}


def list_agents():
    url = '{ep}/agents'.format(ep=endpoint)
    
    r = requests.get(url, headers=headers)
    
    return r.json()


def list_agent(agent_id):
    url = '{ep}/agents/{agid}'.format(ep=endpoint, agid=agent_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    
    

def list_agent_tokens():
    url = '{ep}/agent_tokens'.format(ep=endpoint)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    

def create_agent_token(label=""):
    url = '{ep}/agent_tokens'.format(ep=endpoint)
    
    payload = {
        "label": label
    }
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code == 201:
        return True
    else:
        return r.json()
    
    
    
    
# http://docs.rackspace.com/cm/api/v1.0/cm-devguide/content/maas-core-agents-service-calls.html
# http://docs.rackspace.com/cm/api/v1.0/cm-devguide/content/service-agent-tokens.html