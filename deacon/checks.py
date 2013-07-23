import requests
import json
from copy import deepcopy

from auth import token, endpoint
from entities import get_entity, get_entities

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

template = \
{
    "label": "a label",
    "type": "a type",
    "details": "some details",
    "monitoring_zones_poll": [ 
        "mzdfw", 
        "mzord",
        "mziad",
        "mzlon",
        "mzhkg",
        "mzsyd" 
    ],
    "timeout": 15,
    "period": 60,
    "target_alias": "default"
}

def create_ping_check(entity_id, target_alias):
    url = "{ep}/entities/{eid}/checks".format(ep=endpoint, eid=entity_id)
    
    payload = deepcopy(template)
    
    specifics = { 
        "label": "Ping check for {0}".format(target_alias), 
        "type": "remote.ping", 
        "details": {
            "count": 10
        },
        'target_alias': target_alias
    }
    
    payload.update(specifics)
    print(payload)
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code != 201:
        return r.json()
    else:
        return r.headers['Location']


def list_checks(entity_id):
    url = "{ep}/entities/{eid}/checks".format(ep=endpoint, eid=entity_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    

def delete_check(entity_id, check_id):
    url = "{ep}/entities/{eid}/checks/{cid}".format(ep=endpoint, eid=entity_id, cid=check_id)
    
    r = requests.delete(url, headers=headers)
    
    if r.status_code != 204:
        return r.json()
    else:
        return True
    
    
def create_ping_checks_all_aliases(entity_id):
    """Create ping checks on all interfaces for an entity."""
    
    e = get_entity(entity_id)
    for alias in e['ip_addresses']:
        create_ping_check(e['id'], alias)


def create_ping_checks_all_aliases_all_entities():
    """Create ping checks on all interfaces for all entities."""
    
    ents = get_entities()['values']
    
    for ent in ents:
        create_ping_checks_all_aliases(ent['id'])
    