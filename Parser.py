import re

from Models import Link, Demand, DemandPath

# File path
net4_file_path = "net4.txt"
net12_1_file_path = "net12_1.txt"

# Patterns for regular expressions
regex_pattern_links = r'\d{1,2} \d{1,2} \d{1,2} \d{1,2} \d{1,2}'
regex_pattern_demands = r'\d{1,2} \d{1,2} \d{1,2}\n\d{1,2}\n^[\s\S]*?(?=\n{2,})'


# Pass a string containing part of file with links to get list of Link objects
def get_links_list_from_file(__net4_string_links):
    # Private variable List for holdings Link objects
    __list_of_links = list()

    # Find all matching links, add them to list
    list_of_link_strings = re.findall(regex_pattern_links, __net4_string_links)

    # For each link on list, split values and make a Link object
    for item in list_of_link_strings:
        current_item = item.split()
        __list_of_links.append(
            Link(current_item[0], current_item[1], current_item[2], current_item[3], current_item[4]))

    # Print all items in list
    for i in range(0, len(__list_of_links)):
        print("Start node: {}, End node: {}, Number of modules: {}, Module cost: {}, Link module: {}"
              .format(__list_of_links[i].start_node,
                      __list_of_links[i].end_node,
                      __list_of_links[i].number_of_modules,
                      __list_of_links[i].module_cost,
                      __list_of_links[i].link_module))

    return __list_of_links


# Pass a string containing part of file with demands and demand paths to get list of Demand objects
def get_demands_from_file(__net4_string_demands):
    # Private variable for storing list of demands
    __list_of_demands = list()

    # List with all demands and demand paths found with regex
    list_demands_demand_paths = re.findall(regex_pattern_demands, __net4_string_demands, re.MULTILINE)

    for item in list_demands_demand_paths:
        # Split lines
        __current_item = item.splitlines()  # Split each item found by regex by lines
        __current_item_line1 = __current_item[0].split()  # Line contains start node, end node, demand volume
        __number_of_demand_paths = int(__current_item[1])

        __list_of_demand_paths = list()

        for i in range(2, 2 + __number_of_demand_paths):
            __links_ids = __current_item[i].split()  # Make a list with demand path links ids
            __links_ids.pop(0)  # Delete first element, because it is demand path id
            __list_of_demand_paths.append(DemandPath(i - 1,  # Demand path id (starts with 1)
                                                     __links_ids))  # List of demand path links

        __list_of_demands.append(Demand(__current_item_line1[0],  # Start node
                                        __current_item_line1[1],  # End node
                                        __current_item_line1[2],  # Demand volume
                                        __number_of_demand_paths,
                                        __list_of_demand_paths))
    return __list_of_demands


# Open txt file
with open(net4_file_path, "r") as net4_file:
    # Split file string to 2 strings, each for links and demands
    net4_string_links, net4_string_demands = net4_file.read().split("-1")

# List for holdings Link objects, get Link objects from txt string
# list_of_links = get_links_list_from_file(net4_string_links)

list_of_demands = get_demands_from_file(net4_string_demands)

# Print all items in list
for ix in range(0, len(list_of_demands)):
    print("Start node: {}, End node: {}, Demand volume: {}, Number of demand paths: {},"
          " Demand path 1 id: {}, Demand path 1 links {}"
          .format(list_of_demands[ix].start_node,
                  list_of_demands[ix].end_node,
                  list_of_demands[ix].demand_volume,
                  list_of_demands[ix].number_of_demand_paths,
                  list_of_demands[ix].list_of_demand_paths[0].demand_path_id,
                  list_of_demands[ix].list_of_demand_paths[0].link_id_list
                  ))
