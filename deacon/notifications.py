import json
import requests

from auth import endpoint, token

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}


def list_notifications():
    url = '{ep}/notifications'.format(ep=endpoint)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    

def list_notification_plans():
    url = '{ep}/notification_plans'.format(ep=endpoint)
    
    r = requests.get(url, headers=headers)
    
    return r.json()


def create_notification(payload):
    url = '{ep}/notifications'.format(ep=endpoint)
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code != 201:
        return r.json()
    else:
        return r.headers['Location']
    
    
def create_email_notification():
    payload = {
        'label': 'email_actionlogs-alerts',
        'details': {
            'address': 'actionlogs-alerts@lists.rackspace.com'
        },
        'type': 'email'
    }
    
    create_notification(payload)
    
def create_notification_plan(label, nt_ok, nt_warning, nt_critical):
    """Need notification IDs to come in as lists."""
    
    url = '{ep}/notification_plans'.format(ep=endpoint)
    
    payload = {
        "label": label,
        "critical_state": nt_critical,
        "warning_state": nt_warning,
        "ok_state": nt_ok
    }
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code != 201:
        return r.json()
    else:
        return r.headers['Location']
    
    
def update_notification_plan(np_id):
    url = '{ep}/notification_plans/{np}'.format(ep=endpoint, np=np_id)
    
    payload = {
        "label": "email_actionlogs-alerts",
        "critical_state": [ "nt5vQZSfDg" ],
        "warning_state": [ "nt5vQZSfDg" ],
        "ok_state": [ "nt5vQZSfDg" ]
    }
    
    r = requests.put(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code != 204:
        return r.json()
    else:
        return True
        
def test_existing_notification(nt_id):
    url = '{ep}/notifications/{nt}/test'.format(ep=endpoint, nt=nt_id)
    
    r = requests.post(url, headers=headers)
    
    return r.json()
    

def discover_alarm_notification_history(entity_id, alarm_id):
    url = '{ep}/entities/{eid}/alarms/{aid}/notification_history'.format(ep=endpoint, eid=entity_id, aid=alarm_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    

def list_alarm_notification_history(entity_id, alarm_id, check_id):
    url = '{ep}/entities/{eid}/alarms/{aid}/notification_history/{cid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id, cid=check_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    
    
def get_alarm_notification_history(entity_id, alarm_id, check_id, uuid):
    url = '{ep}/entities/{eid}/alarms/{aid}/notification_history/{cid}/{uuid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id, cid=check_id, ud=uuid)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    