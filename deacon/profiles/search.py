import deacon.checks as checks
import deacon.alarms as alarms


def create_es_monitors(entity_id, address, notif_plan):
    filename = 'elasticsearch.py'
    
    #create all checks for metrics!

    ch_cluster_health = checks.create_plugin_check(entity_id, filename, label="ES Cluster", args=['-H', address, '--cluster-health'])
    ch_stats_store = checks.create_plugin_check(entity_id, filename, label="ES Store", args=['-H', address, '--stats-store'])
    ch_stats_indexing = checks.create_plugin_check(entity_id, filename, label="ES Indexing", args=['-H', address, '--stats-indexing'])
    ch_stats_get = checks.create_plugin_check(entity_id, filename, label = "ES Get", args=['-H', address, '--stats-get'])
    ch_stats_search = checks.create_plugin_check(entity_id, filename, label="ES Search", args=['-H', address, '--stats-search'])
    ch_stats_docs = checks.create_plugin_check(entity_id, filename, label="ES Docs", args=['-H', address, '--stats-docs'])

    #alarm on what...
    alarms.create_es_cluster_alarm(entity_id, ch_cluster_health, notif_plan)
    alarms.create_es_num_nodes_alarm(entity_id, ch_cluster_health, notif_plan)