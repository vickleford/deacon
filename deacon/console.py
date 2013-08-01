from deacon.auth import *
from deacon.checks import *
from deacon.entities import *
from deacon.alarms import *
from deacon.metrics import *
from deacon.notifications import *
from deacon.monitoring_zones import *
from deacon.agent import *


def monitor_api_index(entity_id, notif_plan):
    e = get_entity(entity_id)
    
    personality = {
        "url": "https://{0}/".format(e['label']),
        "body": "Not Found"
    }
    
    check = create_http_check(entity_id, "API Index", personality)
    print("created check: {0}".format(check))
    check_id = check.split('/')[8]
    
    criteria = """
    # 604800 seconds in 1 week
    # 1814400 seconds in 3 weeks
    if (metric["cert_end_in"] < 1814400) {
        return new AlarmStatus(WARNING, "Cert to expire in #{cert_end_in} seconds");
    }
    if (metric["cert_end_in"] < 604800) {
        return new AlarmStatus(CRITICAL, "Cert to expire in #{cert_end_in} seconds");
    }
    if (metric["code"] != "404") {
        return new AlarmStatus(WARNING, "Got response code #{code}");
    }
    if (metric["body_match"] != "Not Found") {
        return new AlarmStatus(WARNING, "Didn't get expected body match");
    }
    if (metric["tt_firstbyte"] > 7000) {
        return new AlarmStatus(WARNING, "Check took #{duration}ms");
    }
    return new AlarmStatus(OK);
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "API Index", criteria)
    print("created alarm: {0}".format(alarm))
    
    
def monitor_ui_index(entity_id, notif_plan):
    e = get_entity(entity_id)
    
    personality = {
        "url": "https://{0}/".format(e['label']),
        "body": "script type"
    }
    
    check = create_http_check(entity_id, "UI Index", personality)
    print("created check: {0}".format(check))
    
    check_id = check.split('/')[8]
    
    criteria = """
    # 604800 seconds in 1 week
    # 1814400 seconds in 3 weeks
    if (metric["cert_end_in"] < 1814400) {
        return new AlarmStatus(WARNING, "Cert to expire in #{cert_end_in} seconds");
    }
    if (metric["cert_end_in"] < 604800) {
        return new AlarmStatus(CRITICAL, "Cert to expire in #{cert_end_in} seconds");
    }
    if (metric["code"] != "200") {
        return new AlarmStatus(WARNING, "Got response code #{code}");
    }
    if (metric["body_match"] != "script type") {
        return new AlarmStatus(WARNING, "Didn't get expected body match");
    }
    if (metric["tt_firstbyte"] > 7000) {
        return new AlarmStatus(WARNING, "Check took #{duration}ms");
    }
    return new AlarmStatus(OK);
    """
    
    alarm = create_alarm(entity_id, check_id, notif_plan, "UI Index", criteria)
    print("created alarm: {0}".format(alarm))
    
    
    
def create_api_lb_monitors(entity_id, notif_plan):
    ping_check = create_ping_check(entity_id)
    ping_check_id = ping_check.split('/')[8]

    create_ping_alarm(entity_id, ping_check_id, notif_plan)

    monitor_api_index(entity_id, notif_plan)
    

def create_ui_lb_monitors(entity_id, notif_plan):
    ping_check = create_ping_check(entity_id)
    ping_check_id = ping_check.split('/')[8]
    
    create_ping_alarm(entity_id, ping_check_id, notif_plan)
    
    monitor_ui_index(entity_id, notif_plan)
    
    
def add_missing_ping_monitors(notif_plan):
    for e in get_entities()['values']:
        has_ping = False
        for c in list_checks(e['id'])['values']:
            if "Ping" in c['label']:
                has_ping = True
        if not has_ping:
            print("creating ping checks and alarms on {0}".format(e['label']))
            check = create_ping_check(e['id'])
            check_id = check.split('/')[8]
            create_ping_alarm(e['id'], check_id, notif_plan)