import json
import requests

from entities import get_entities
from checks import list_checks
from auth import token, endpoint

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

def list_alarms(entity_id):
    url = '{ep}/entities/{eid}/alarms'.format(ep=endpoint, eid=entity_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    
    
def show_alarms(entity_id):
    pass


def delete_alarm(entity_id, alarm_id):
    url = '{ep}/entities/{eid}/alarms/{aid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id)
    
    r = requests.delete(url, headers=headers)
    
    if r.status_code != 204:
        return r.json()
    else:
        return True
    

def get_alarm(entity_id, alarm_id):
    url = '{ep}/entities/{eid}/alarms/{aid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()


def get_available_history(entity_id, alarm_id):
    url = '{ep}/entities/{eid}/alarms/{aid}/notification_history'.format(ep=endpoint, eid=entity_id, aid=alarm_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()


def get_alarm_history(entity_id, alarm_id, check_id):
    url = '{ep}/entities/{eid}/alarms/{aid}/notification_history/{cid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id, cid=check_id)

    r = requests.get(url, headers=headers)

    return r.json()

    
def create_alarm(entity_id, check_id, notif_plan, criteria):
    payload = \
    {
        "check_id": check_id,
        "criteria": criteria, 
        "notification_plan_id": notif_plan
    }
    
    url = '{ep}/entities/{eid}/alarms'.format(ep=endpoint, eid=entity_id)
        
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code != 201:
        return r.json()
    else:
        return r.headers['Location']


def update_alarm(entity_id, alarm_id):
    url = '{ep}/entities/{eid}/alarms/{aid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id)
    
    new_criteria = """
    if (metric["available"] >= 80) {
        return new AlarmStatus(OK, "Back to #{available}% success rate"); 
    }
    if (metric["available"] >= 60) {
        return new AlarmStatus(WARNING, "Getting #{available}% packet loss");
    }
    return new AlarmStatus(CRITICAL, "Getting #{available}% packet loss");
    """

    payload = {"criteria": new_criteria}

    r = requests.put(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code != 204:
        return r.json()
    else:
        return True
    

def create_ping_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if (metric["available"] >= 80) {
        return new AlarmStatus(OK, "Back to #{available}% success rate"); 
    }
    if (metric["available"] >= 60) {
        return new AlarmStatus(WARNING, "Getting #{available}% packet loss");
    }
    return new AlarmStatus(CRITICAL, "Getting #{available}% packet loss");
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, criteria)
    
    return alarm


def create_ping_alarms(np_id):
    ents = get_entities()['values']
    for ent in ents:
        for chk in list_checks(ent['id'])['values']:
            create_ping_alarm(ent['id'], chk['id'], np_id)