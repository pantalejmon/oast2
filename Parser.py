import re

from Models import Link, Demand, DemandPath

# File path
net4_file_path = "net4.txt"
net12_1_file_path = "net12_1.txt"
net12_2_file_path = "net12_2.txt"

# Patterns for regular expressions
regex_pattern_links = r'\d{1,2} \d{1,2} \d{1,2} \d{1,2} \d{1,2}'
regex_pattern_demands = r'\d{1,2} \d{1,2} \d{1,2}\n\d{1,2}\n^[\s\S]*?(?=\n{2,})'

# Use ONLY on second part of file string without GLOBAL modifier (only MULTILINE),
# it will get first number and number of demands is first in second part of file, after -1
# Use with re.search
regex_pattern_number_of_demands = r'^\d{1,3}$'
regex_pattern_number_of_links = r'^\d{1,3}$'


# Pass a string containing part of file with links to get list of Link objects
def get_links_list_from_file(__net_string_links):
    # Private variable List for holdings Link objects
    __list_of_links = list()

    # Find all matching links, add them to list
    list_of_link_strings = re.findall(regex_pattern_links, __net_string_links)

    # For each link on list, split values and make a Link object
    for item in list_of_link_strings:
        current_item = item.split()
        __list_of_links.append(
            Link(start_node=current_item[0],
                 end_node=current_item[1],
                 number_of_modules=int(current_item[2]),
                 module_cost=int(current_item[3]),
                 link_module=int(current_item[4])))

    return __list_of_links


# Pass a string containing part of file with demands and demand paths to get list of Demand objects
def get_demands_from_file(__net_string_demands):
    # Private variable for storing list of demands
    __list_of_demands = list()

    # List with all demands and demand paths found with regex
    list_demands_and_demand_paths = re.findall(
        regex_pattern_demands, __net_string_demands, re.MULTILINE)

    # Loop through all items found by regex
    for item in list_demands_and_demand_paths:
        # Split lines
        __current_item = item.splitlines()  # Split each item found by regex by lines
        # First line contains start node, end node, demand volume
        __current_item_line1 = __current_item[0].split()
        # Second line contains number of demand paths
        __number_of_demand_paths = int(__current_item[1])

        __list_of_demand_paths = list()

        # Start looping at 2, it is the first line with demands
        for i in range(2, 2 + __number_of_demand_paths):
            # Make a list with demand path links ids
            __links_ids = __current_item[i].split()
            # Delete first element, it is demand path id, we don't need it on list of link ids
            __links_ids.pop(0)
            # Construct Demand Path object, append it to list of demand paths
            __list_of_demand_paths.append(DemandPath(i - 1,  # Demand path id (starts with 1)
                                                     __links_ids))  # List of demand path links

        __list_of_demands.append(Demand(start_node=__current_item_line1[0],  # Start node
                                        # End node
                                        end_node=__current_item_line1[1],
                                        # Demand volume
                                        demand_volume=int(
                                            __current_item_line1[2]),
                                        number_of_demand_paths=int(
                                            __number_of_demand_paths),
                                        list_of_demand_paths=__list_of_demand_paths))
    return __list_of_demands


# Pass first part of file string (splitted by -1) containing links
def get_number_of_links(__net_string_links):
    return int(re.search(regex_pattern_number_of_links, __net_string_links, re.MULTILINE).group())


# Pass second part of file string (splitted by -1) containing demands
def get_number_of_demands(__net_string_demands):
    return int(re.search(regex_pattern_number_of_demands, __net_string_demands, re.MULTILINE).group())
