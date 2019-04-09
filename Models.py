# Class representing single link
class Link:

    # Values specific to instance
    def __init__(self, start_node, end_node, number_of_modules, module_cost, link_module):
        self.start_node = start_node
        self.end_node = end_node
        self.number_of_modules = number_of_modules
        self.module_cost = module_cost
        self.link_module = link_module

    def print_link_properties(self):
        print("Start node: {}, End node: {}, Number of modules: {}, Module cost: {}, Link module: {}"
              .format(self.start_node,
                      self.end_node,
                      self.number_of_modules,
                      self.module_cost,
                      self.link_module))


# Class representing a single demand
class Demand:

    # Values specific to instance
    def __init__(self, start_node, end_node, demand_volume, number_of_demand_paths, list_of_demand_paths):
        self.start_node = start_node
        self.end_node = end_node
        self.demand_volume = demand_volume
        self.number_of_demand_paths = number_of_demand_paths
        self.list_of_demand_paths = list_of_demand_paths


# Class representing single demand path
class DemandPath:

    # Values specific to instance
    def __init__(self, demand_path_id, link_id_list):
        self.demand_path_id = demand_path_id
        self.link_id_list = link_id_list  # List of link ids that construct demand path
