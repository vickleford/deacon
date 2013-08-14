import deacon.checks as checks
import deacon.alarms as alarms
from deacon.entities import get_entity


def monitor_api_index(entity_id, notif_plan):
    e = get_entity(entity_id)
    
    personality = {
        "url": "https://{0}/".format(e['label']),
        "body": "Not Found"
    }
    
    check_id = checks.create_http_check(entity_id, "API Index", personality)
    print("created check: {0}".format(check_id))
    
    criteria = """
    :set consecutiveCount=2
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
    
    alarm = alarms.create_alarm(entity_id, check_id, notif_plan, "API Index", criteria)
    print("created alarm: {0}".format(alarm))


def monitor_api_healthcheck(entity_id, notif_plan):
    e = get_entity(entity_id)
    
    personality = {
        "url": "https://{0}/healthcheck".format(e['label']),
        "body_matches": {
            "hbase": "\"hbase\": true",
            "mongo": "\"mongo\": true"
        }
    }
    
    check_id = checks.create_http_check(e['id'], "API Healthcheck", personality)
    
    criteria = """
    if (metric["body_match_mongo"] != "\\"mongo\\": true") {
        return new AlarmStatus(CRITICAL, "Can't connect to mongo");
    }
    return new AlarmStatus(OK);
    """
    
    alarm = alarms.create_alarm(e['id'], check_id, notif_plan, "API Healthcheck", criteria)