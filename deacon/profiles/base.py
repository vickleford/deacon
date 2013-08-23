import deacon.checks as checks
import deacon.alarms as alarms


def make_default_monitors(entity_id, notif_id):
    """Create stock monitors that every system should get."""
    
    #
    # create checks
    #
    ch_ssh = checks.create_ssh_check(entity_id)
    for iface in [ 'eth0', 'eth1', 'eth2' ]:
        ch_net = checks.create_network_check(entity_id, target=iface)
        # create alarm for interface here
    ch_disk = checks.create_disk_check(entity_id)
    ch_mem = checks.create_memory_check(entity_id)
    ch_load = checks.create_load_average_check(entity_id)
    ch_fs = checks.create_filesystem_check(entity_id)
    ch_cpu = checks.create_cpu_check(entity_id)
    ch_ping = checks.create_ping_check(entity_id)
    
    #
    # create alarms
    #
    alarms.create_ssh_alarm(entity_id, ch_ssh, notif_id)
    alarms.create_memory_alarm(entity_id, ch_mem, notif_id)
    alarms.create_load_average_alarm(entity_id, ch_load, notif_id)
    alarms.create_filesystem_alarm(entity_id, ch_fs, notif_id)
    alarms.create_cpu_alarm(entity_id, ch_cpu, notif_id)
    alarms.create_ping_alarm(entity_id, ch_ping, notif_id)
    

