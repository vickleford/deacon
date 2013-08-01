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


def create_check(entity_id, timeout=15, period=60, mzpoll=[ "mzdfw", "mzord", "mziad", "mzlon", "mzhkg", "mzsyd" ], extras={}):
    """
    Create a check and return the link to it.
    
    Expecting extras to have things like type, label, target_alias, details, etc
    """
    
    payload = {
        "monitoring_zones_poll": mzpoll,
        "timeout": timeout,
        "period": period,
        "target_alias": "public0_v4"
    }

    payload.update(extras)
    
    # agent checks cannot have any monitoring zones
    if "agent" in payload['type']:
        del payload['monitoring_zones_poll']
        del payload['target_alias']
    
    url = '{ep}/entities/{eid}/checks'.format(ep=endpoint, eid=entity_id)
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code == 201:
        return r.headers['Location']
    else:
        why = r.json()
        if "no such alias public" in why['details']:
            payload.update({"target_alias": "public1_v4"})
            print("Retrying with alternate target alias")
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            if r.status_code == 201:
                return r.headers['Location']
            else:
                return r.json()


def create_http_check(entity_id, label, details):
    personality = {
        "type": "remote.http",
        "label": label,
        "details": details
    }
    
    return create_check(entity_id, extras=personality)


def create_mongo_check(entity_id, url, target_alias='alvn0_v4'):
    personality = {
        "type": "remote.http",
        "label": "MongoDB REST",
        "details": {
            "url": url,
            "body": "total_rows",
        },
        "target_alias": target_alias
    }
    
    return create_check(entity_id, extras=personality)            
    
    
def create_ssh_check(entity_id, port=22):
    personality = {
        "type": "remote.ssh",
        "label": "OpenSSH Check",
        "details": {
            "port": port,
        }
    }
    
    return create_check(entity_id, extras=personality)
    
    
def create_network_check(entity_id, target='eth0'):
    personality = {
        "type": "agent.network",
        "label": "{i} Network Check".format(i=target),
        "details": {
            "target": target
        }
    }
    
    return create_check(entity_id, extras=personality)
    

def create_disk_check(entity_id, target='/dev/xvda1'):
    personality = {
        "type": "agent.disk",
        "details": {
            "target": target
        },
        "label": "{t} Disk Check".format(t=target)
    }
    
    return create_check(entity_id, extras=personality)
        

def create_memory_check(entity_id):
    personality = {
        "type": "agent.memory",
        "label": "Memory"
    }
    
    return create_check(entity_id, extras=personality)
    

def create_load_average_check(entity_id):
    personality = {
        "type": "agent.load_average",
        "label": "Load Average"
    }
    
    return create_check(entity_id, extras=personality)


def create_filesystem_check(entity_id):
    personality = {
        "type": "agent.filesystem",
        "details": {
            "target": "/"
        },
        "label": "Filesystem Check"
    }
    
    return create_check(entity_id, extras=personality)
    

def create_cpu_check(entity_id):
    personality = { 
        "type": "agent.cpu",
        "label": "CPU Check",
    }
    
    return create_check(entity_id, extras=personality)


def create_ping_check(entity_id, target_alias='public0_v4'):
    url = "{ep}/entities/{eid}/checks".format(ep=endpoint, eid=entity_id)

    personality = { 
        "label": "Ping check for {0}".format(target_alias), 
        "type": "remote.ping", 
        "details": {
            "count": 5
        },
        'target_alias': target_alias
    }

    return create_check(entity_id, extras=personality)


def get_check(entity_id, check_id):
    url = '{ep}/entities/{eid}/checks/{cid}'.format(ep=endpoint, eid=entity_id, cid=check_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()


def old_create_ping_check(entity_id, target_alias):
    url = "{ep}/entities/{eid}/checks".format(ep=endpoint, eid=entity_id)
    
    payload = deepcopy(template)
    
    specifics = { 
        "label": "Ping check for {0}".format(target_alias), 
        "type": "remote.ping", 
        "details": {
            "count": 5
        },
        'target_alias': target_alias
    }
    
    payload.update(specifics)

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code != 201:
        return r.json()
    else:
        return r.headers['Location']


def list_checks(entity_id):
    url = "{ep}/entities/{eid}/checks".format(ep=endpoint, eid=entity_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()


def show_checks(entity_id):
    row = "{:<15}{:<40}{:<40}{:<15}{:<15}{:<10}{:<10}"
    chks = list_checks(entity_id)
    print(row.format('ID', 'Label', 'Target', 'Created', 'Updated', 'Period', 'Disabled'))
    for value in chks['values']:
        print(row.format(value['id'], value['label'], value['target_alias'], value['created_at'], value['updated_at'], value['period'], bool(value['disabled'])))



def delete_check(entity_id, check_id):
    url = "{ep}/entities/{eid}/checks/{cid}".format(ep=endpoint, eid=entity_id, cid=check_id)
    
    r = requests.delete(url, headers=headers)
    
    if r.status_code != 204:
        return r.json()
    else:
        return True
    
    
def create_ping_checks_public_aliases(entity_id):
    """Create ping checks on all interfaces for an entity."""
    
    e = get_entity(entity_id)
    for alias in e['ip_addresses']:
        if 'public' in alias:
            create_ping_check(e['id'], alias)


def create_ping_checks_public_aliases_all_entities():
    """Create ping checks on all interfaces for all entities."""
    
    ents = get_entities()['values']
    
    for ent in ents:
        create_ping_checks_all_aliases(ent['id'])


def destroy_all_checks(entity_id, type):
    chks = list_checks(entity_id)
    for chk in chks['values']:
        if chk['type'] == type:
            url = '{ep}/entities/{eid}/checks/{cid}'.format(ep=endpoint, eid=entity_id, cid=chk['id'])
            r = requests.delete(url, headers=headers)
            if r.status_code != 204:
                print(r.json())
            else:
                print("Deleted {cid} from {eid}".format(cid=chk['id'], eid=entity_id))
    
            
def destroy_some_checks_all_entities(type):
    # type example: remote.ping
    ents = get_entities()['values']
    
    for ent in ents:
        destroy_all_checks(ent['id'], type)
        
        
def update_check(entity_id, check_id, payload):
    url = "{ep}/entities/{eid}/checks/{cid}".format(ep=endpoint, eid=entity_id, cid=check_id)

    r = requests.put(url, data=json.dumps(payload), headers=headers)

    if r.status_code != 204:
        return r.json()
    else:
        return True