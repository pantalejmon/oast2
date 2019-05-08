# Class representing single link
class Link:

    # Values specific to instance
    def __init__(self, start_node, end_node, number_of_modules, module_cost, link_module):
        self.start_node = start_node  # as Int
        self.end_node = end_node  # as Int
        self.number_of_modules = number_of_modules  # as Int
        self.module_cost = module_cost  # as Int
        self.link_module = link_module  # as Int

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
        self.start_node = start_node  # as String
        self.end_node = end_node  # as String
        self.demand_volume = demand_volume  # as Int
        self.number_of_demand_paths = number_of_demand_paths  # as Int
        self.list_of_demand_paths = list_of_demand_paths  # First item at position 0

    def print_demand_properties(self):
        print("Start node: {}, End node: {}, Demand volume: {}, \nNumber of demand paths: {}"
              .format(self.start_node,
                      self.end_node,
                      self.demand_volume,
                      self.number_of_demand_paths))
        for i in range(0, self.number_of_demand_paths):
            self.list_of_demand_paths[i].print_demand_path_properties()


# Class representing single demand path
class DemandPath:

    # Values specific to instance
    def __init__(self, demand_path_id, link_id_list):
        self.demand_path_id = demand_path_id  # as Int
        self.link_id_list = link_id_list  # List of link ids (Strings) that construct demand path

    def print_demand_path_properties(self):
        print("Demand path id: {}, Demand path links ids list: {}".format(
            self.demand_path_id,
            self.link_id_list))


# Representation of single Gene
class Gene:

    def __init__(self, list_of_alleles, demand_volume):
        self.list_of_alleles = list_of_alleles  # as list of Int
        # Sum of all values on list of alleles should be the same as demand_volume
        self.demand_volume = demand_volume  # as Int


# Representation of single Chromosome used is Evolutionary Algorithm
class Chromosome:

    # Values specific to instance
    def __init__(self, list_of_genes, fitness_dap, fitness_ddap):
        self.list_of_genes = list_of_genes  # as list of Int
        self.fitness_dap = fitness_dap  # as Int
        self.fitness_ddap = fitness_ddap  # as Int
