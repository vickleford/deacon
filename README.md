Truthfully, I'm really just using it from ipython as a script suite right now--yes, calling the functions individually.

---

This example creates ping checks for all network interfaces on all entities on an account with a bunch of hard-coded defaults.

    aluminum13:deacon$ python
    Python 2.7.3 (default, Oct 22 2012, 06:12:28)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from deacon import checks
    >>> checks.create_ping_checks_all_aliases_all_entities()
    {'target_alias': u'access_ip0_v6', 'period': 60, 'label': 'Ping check for access_ip0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'alvn0_v4', 'period': 60, 'label': 'Ping check for alvn0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip1_v4', 'period': 60, 'label': 'Ping check for access_ip1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public0_v6', 'period': 60, 'label': 'Ping check for public0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'private0_v4', 'period': 60, 'label': 'Ping check for private0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public1_v4', 'period': 60, 'label': 'Ping check for public1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip0_v6', 'period': 60, 'label': 'Ping check for access_ip0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'alvn0_v4', 'period': 60, 'label': 'Ping check for alvn0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip1_v4', 'period': 60, 'label': 'Ping check for access_ip1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public0_v6', 'period': 60, 'label': 'Ping check for public0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'private0_v4', 'period': 60, 'label': 'Ping check for private0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public1_v4', 'period': 60, 'label': 'Ping check for public1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip0_v6', 'period': 60, 'label': 'Ping check for access_ip0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'alvn0_v4', 'period': 60, 'label': 'Ping check for alvn0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip1_v4', 'period': 60, 'label': 'Ping check for access_ip1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public0_v6', 'period': 60, 'label': 'Ping check for public0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'private0_v4', 'period': 60, 'label': 'Ping check for private0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public1_v4', 'period': 60, 'label': 'Ping check for public1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip0_v6', 'period': 60, 'label': 'Ping check for access_ip0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'alvn0_v4', 'period': 60, 'label': 'Ping check for alvn0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip1_v4', 'period': 60, 'label': 'Ping check for access_ip1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public0_v6', 'period': 60, 'label': 'Ping check for public0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'private0_v4', 'period': 60, 'label': 'Ping check for private0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public1_v4', 'period': 60, 'label': 'Ping check for public1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip0_v6', 'period': 60, 'label': 'Ping check for access_ip0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip1_v4', 'period': 60, 'label': 'Ping check for access_ip1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public0_v6', 'period': 60, 'label': 'Ping check for public0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'private0_v4', 'period': 60, 'label': 'Ping check for private0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public1_v4', 'period': 60, 'label': 'Ping check for public1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip0_v6', 'period': 60, 'label': 'Ping check for access_ip0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'alvn0_v4', 'period': 60, 'label': 'Ping check for alvn0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public0_v4', 'period': 60, 'label': 'Ping check for public0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip1_v4', 'period': 60, 'label': 'Ping check for access_ip1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'private0_v4', 'period': 60, 'label': 'Ping check for private0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public1_v6', 'period': 60, 'label': 'Ping check for public1_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip0_v6', 'period': 60, 'label': 'Ping check for access_ip0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'alvn0_v4', 'period': 60, 'label': 'Ping check for alvn0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'access_ip1_v4', 'period': 60, 'label': 'Ping check for access_ip1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public0_v6', 'period': 60, 'label': 'Ping check for public0_v6', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'private0_v4', 'period': 60, 'label': 'Ping check for private0_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    {'target_alias': u'public1_v4', 'period': 60, 'label': 'Ping check for public1_v4', 'details': {'count': 10}, 'timeout': 15, 'monitoring_zones_poll': ['mzdfw', 'mzord', 'mziad', 'mzlon', 'mzhkg', 'mzsyd'], 'type': 'remote.ping'}
    >>> ^D
    
---
    
This example creates load average checks then creates alarms for those checks

    aluminum13:deacon$ python
    Python 2.7.3 (default, Oct 22 2012, 06:12:28)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from deacon.console import *
    >>> for e in get_entities()['values']:
    ...     create_load_average_check(e['id'])
    ...
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/en39PNSYuy/checks/chdtzrsn5n'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/en9SlBPL18/checks/chlWrvKQtY'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/enACj4ASei/checks/ch2zc90RrQ'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/enB7HpTnyX/checks/chUcbp4W4r'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/eneoftdl90/checks/chDD54W4cu'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/envQh1t1BX/checks/chh1WCkEeF'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/enz9bF86Rf/checks/chSArBny5X'
    >>> for e in get_entities()['values']:
    ...     for c in list_checks(e['id'])['values']:
    ...         if c['type'] == 'agent.load_average':
    ...             create_load_average_alarm(e['id'], c['id'], 'npXXXXXXXX')
    ...
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/en39PNSYuy/alarms/aluWnWLDcq'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/en9SlBPL18/alarms/alUZQFLqw1'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/enACj4ASei/alarms/alsehZKA6f'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/enB7HpTnyX/alarms/alfYqkPFia'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/eneoftdl90/alarms/aluRqhhmnC'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/envQh1t1BX/alarms/alludq89ww'
    'https://monitoring.api.rackspacecloud.com/v1.0/xxxxxx/entities/enz9bF86Rf/alarms/alJNkHOYA1'
    >>>
    
---
    
This example updates the count on all your ping checks

    aluminum13:deacon$ python
    Python 2.7.3 (default, Oct 22 2012, 06:12:28)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from deacon.console import *
    >>> for e in get_entities()['values']:
    ...     for c in list_checks(e['id'])['values']:
    ...             if c['type'] == 'remote.ping':
    ...                     update_check(e['id'], c['id'], {"details": { "count": 5 }})
    ...
    True
    True
    True
    True
    True
    True
    True