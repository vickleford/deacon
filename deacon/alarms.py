import json
import requests

from auth import token, endpoint

headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}

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
    
    
def create_ping_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if (metric["duration"] >= 2) {
        return {new AlarmStatus(OK); 
    } 
    return new AlarmStatus(CRITICAL);
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, criteria)
    
    return alarm
