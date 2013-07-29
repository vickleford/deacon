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

    
def create_alarm(entity_id, check_id, notif_plan, label, criteria):
    payload = \
    {
        "label": label,
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


def create_mongo_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if (metric["code"] != 200 && metric["body_match"] != "total_rows") {
        return new AlarmStatus(WARNING, "Got status code #{code} and matched #{body_match} instead of 'total_rows'");
    }
    if (metric["duration"] >= 2000) {
        return new AlarmStatus(WARNING, "Took #{duration}ms to finish check");
    }
    return new AlarmStatus(OK);
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "Mongo REST", criteria)
    
    return alarm
    
    
def create_ssh_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if (metric["duration"] >= 2500) {
        return new AlarmStatus(WARNING, "SSH daemon took #{duration}ms to respond");
    }
    if (previous(metric["fingerprint"]) != metric["fingerprint"]) {
        return new AlarmStatus(WARNING, "SSH fingerprint changed to #{fingerprint}");
    }
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "OpenSSH", criteria)
    
    return alarm
    
    
def create_memory_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if (percentage(metric["actual_free"], metric["total"]) <= 20) {
        return new AlarmStatus(WARNING, "Actual free RAM too low: #{actual_free} bytes");
    }
    if (percentage(metric["swap_free"], metric["swap_total"]) <= 20) {
        return new AlarmStatus(WARNING,"Free swap too low: #{swap_free} bytes");
    }
    return new AlarmStatus(OK);
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "Memory", criteria)
    
    return alarm
    

def create_load_average_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if (metric["5m"] > 4) {
        return new AlarmStatus(WARNING, "Load Average increased to #{5m}");
    }
    return new AlarmStatus(OK);
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "Load Average", criteria)
    
    return alarm
    

def create_filesystem_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if (percentage(metric["free_files"], metric["files"]) <= 20) {
        return new AlarmStatus(WARNING, "inodes usage exceeded 80%");
    }
    if (percentage(metric["avail"], metric["total"]) <= 20) {
        return new AlarmStatus(WARNING, "Disk usage exceeded 80%");
    }
    return new AlarmStatus(OK);
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "Filesystem", criteria)
    
    return alarm
    

def create_cpu_alarm(entity_id, check_id, notif_plan):
    criteria = """
    if ((metric["max_cpu_usage"] >= 95) && (metric["min_cpu_usage"] <= 10)) {
        return new AlarmStatus(WARNING, "Possible runaway process detected");
    }
    if (metric["wait_percent_average"] >= 65) {
        return new AlarmStatus(WARNING, "Detected high wait status: #{wait_percent_average}%");
    }
    if (metric["usage_average"] >= 90) {
        return new AlarmStatus(WARNING, "Usage average reached #{usage_average}%");
    }
    return new AlarmStatus(OK, "CPU usage stabilized");
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "CPU", criteria)
    
    return alarm


def update_alarm(entity_id, alarm_id, payload):
    url = '{ep}/entities/{eid}/alarms/{aid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id)
    
    r = requests.put(url, data=json.dumps(payload), headers=headers)
    
    if r.status_code == 204:
        return True
    else:
        return r.json()
        

def update_alarm_criteria(entity_id, alarm_id):
    url = '{ep}/entities/{eid}/alarms/{aid}'.format(ep=endpoint, eid=entity_id, aid=alarm_id)
    
    new_criteria = """
    :set consecutiveCount=3
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
    :set consecutiveCount=3
    if (metric["available"] >= 80) {
        return new AlarmStatus(OK, "Back to #{available}% success rate"); 
    }
    if (metric["available"] >= 60) {
        return new AlarmStatus(WARNING, "Getting #{available}% packet loss");
    }
    return new AlarmStatus(CRITICAL, "Getting #{available}% packet loss");
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "Ping", criteria)
    
    return alarm


def create_ping_alarms(np_id):
    ents = get_entities()['values']
    for ent in ents:
        for chk in list_checks(ent['id'])['values']:
            create_ping_alarm(ent['id'], chk['id'], np_id)