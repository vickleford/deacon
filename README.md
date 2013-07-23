Truthfully, I'm really just using it from ipython as a script suite right now--yes, calling the functions individually.

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