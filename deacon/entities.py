import json
import requests

from auth import token, endpoint

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}


def create_entity(label, agent_id=None, ip_addresses=None, metadata=None):
    """
    
    Expecting ip_addresses to be a hash [String,String between 1 and 64 characters long:IPv4 or IPv6 address]
    """
    
    url = "{ep}/entities".format(ep=endpoint)
    
    payload = {
        "label": label,
    }
    
    if agent_id is not None:
        payload.update({"agent_id": agent_id})
    
    if ip_addresses is not None:
        payload.update({"ip_addresses": ip_addresses})
        
    if metadata is not None:
        payload.update({"metadata": metadata})
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code == 201:
        return r.headers['Location']
    else:
        return r.json()


def delete_entity(entity_id):
    url = "{ep}/entities/{eid}".format(ep=endpoint, eid=entity_id)
    
    r = requests.delete(url, headers=headers)
    
    if r.status_code == 204:
        return True
    else:
        return r.json()
    
    
def get_entities():
    url = "{ep}/entities".format(ep=endpoint)
    r = requests.get(url, headers=headers)
    
    return r.json()
    

def get_entity(entity_id):
    url = "{ep}/entities/{eid}".format(ep=endpoint, eid=entity_id)
    r = requests.get(url, headers=headers)
    
    return r.json()
    
    
def show_entities():
    row = "{:<15}{:<40}{:<40}{:<15}{:<15}"
    ents = get_entities()
    print(row.format('ID', 'Label', 'Agent ID', 'Created', 'Updated'))
    for value in ents['values']:
        print(row.format(value['id'], value['label'], value['agent_id'], value['created_at'], value['updated_at']))


def update_entity(entity_id, payload):
    """Update an entity with a payload.
    
    Expect payload to be a dict representing your changes 
    Will get converted to json automatically.
    """

    url = "{ep}/entities/{id}".format(ep=endpoint, id=entity_id)
    r = requests.put(url, data=json.dumps(payload), headers=headers)
    

def agents_to_entities():
    """Search for entities without agent ids and assign the entity name as the agent id.
    
    Best if you named both your entities and agent ids by fqdn.
    """
    
    ents = get_entities()
    
    for ent in ents['values']:
        if ent['agent_id'] == None:
            payload = {'agent_id': ent['label']}
            print("Assigning agent to {e}...".format(e=ent['label']))
            update_entity(ent['id'], payload)
