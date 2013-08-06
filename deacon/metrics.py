import json
import requests
import time

from auth import token, endpoint


headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}


def list_metrics(entity_id, check_id):
    
    url = '{ep}/entities/{eid}/checks/{cid}/metrics'.format(ep=endpoint, eid=entity_id, cid=check_id)
    
    r = requests.get(url, headers=headers)
    
    return r.json()
    
    
def fetch_points(entity_id, check_id, metric_name, params={}):
    
    url = '{ep}/entities/{eid}/checks/{cid}/metrics/{mn}/plot'.format(ep=endpoint, eid=entity_id, cid=check_id, mn=metric_name)
    
    r = requests.get(url, headers=headers, params=params)
    
    return r.json()

    
def logtime_to_timestamp(apachetime):
    """Return the number of seconds since the epoch in UTC
    
    Expecitng a string like "01/Aug/2013:03:45:59" to come in.
    """
    
    format = "%d/%b/%Y:%H:%M:%S"
    
    time_in = time.strptime(apachetime, format)
    
    time_out = time.mktime(time_in)
    
    return int(time_out)
    
def logtime_to_timestamp_ms(apachetime):
    """Return the number of milliseconds since the epoch in UTC
    
    Expecitng a string like "01/Aug/2013:03:45:59" to come in.
    """
    time_in = logtime_to_timestamp(apachetime)
    time_out = time_in*1000
    
    return int(time_out)
    

def timestamp_to_logtime(secs):
    """Convert the seconds since the epoch in UTC to an apache-like log format.
    """
    
    format = "%d/%b/%Y:%H:%M:%S"
    
    time_in = time.gmtime(secs)
    time_out = time.strftime(format, time_in)
    
    return time_out
    
    
def pretty_points(entity_id, check_id, check_name, starttime, stoptime, resolution='FULL'):
    """
    
    Still expecting a date string like "01/Aug/2013:03:45:59" to come in
    
    example:
    pretty_points(e, c, 'mzsyd.tt_connect', '01/Aug/2013:00:40:00', '01/Aug/2013:04:50:00')
    """
    
    time_from = logtime_to_timestamp_ms(starttime)
    time_until = logtime_to_timestamp_ms(stoptime)
    
    params = {
        'from': time_from,
        'to': time_until,
        'resolution': resolution
    }
    
    points = fetch_points(entity_id, check_id, check_name, params)
    
    for p in points['values']:
        print(timestamp_to_logtime(p['timestamp']/1000), p['average'])