import re

from Models import Link, Demand, DemandPath

# File path
net4_file_path = "net4.txt"

# Patterns for regular expressions
regex_pattern_links = r'\d{1,2} \d{1,2} \d{1,2} \d{1,2} \d{1,2}'


# Pass a string containing part of file with links to get list of Link objects
def get_links_list_from_file(__net4_string_links):
    # Private variable List for holdings Link objects
    __list_of_links = list()

    # Find all matching links, add them to list
    list_of_link_strings = re.findall(r'\d{1,2} \d{1,2} \d{1,2} \d{1,2} \d{1,2}', __net4_string_links)

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


# Open txt file
with open(net4_file_path, "r") as net4_file:
    # Split file string to 2 strings, each for links and demands
    net4_string_links, net4_string_demands = net4_file.read().split("-1")

# List for holdings Link objects, get Link objects from txt string
list_of_links = get_links_list_from_file(net4_string_links)
