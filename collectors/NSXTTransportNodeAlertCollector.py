from collectors.AlertCollector import AlertCollector


class NSXTTransportNodeAlertCollector(AlertCollector):

    def __init__(self):
        super().__init__()
        self.vrops_entity_name = 'nsxt_transport_node'
        self.label_names = ['nsxt_mgmt_cluster', 'nsxt_adapter', 'transport_zone_name', 'nsxt_transport_node']
        self.resourcekind = ["TransportNode"]

    def get_resource_uuids(self):
        return self.get_nsxt_transport_nodes_by_target()

    def get_labels(self, resource_id, project_ids):
        return [self.nsxt_transport_nodes[resource_id]['mgmt_cluster_name'],
                self.nsxt_transport_nodes[resource_id]['nsxt_adapter_name'],
                self.nsxt_transport_nodes[resource_id]['transport_zone_name'],
                self.nsxt_transport_nodes[resource_id]['name']] if resource_id in self.nsxt_transport_nodes else []
