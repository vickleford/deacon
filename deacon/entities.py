import json
import requests

from auth import token, endpoint

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

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
