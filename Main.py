import Parser

from EvolutionaryAlgorithm import generate_first_population

with open(Parser.net4_file_path, "r") as net_file:
    # Split file string to 2 strings, each for links and demands
    net_string_links, net_string_demands = net_file.read().split("-1")

    # List for holdings Link objects, get Link objects from txt string
    list_of_links = Parser.get_links_list_from_file(net_string_links)

    # print(Parser.get_number_of_links(net_string_links))
    # print(Parser.get_number_of_demands(net_string_demands))

    list_of_demands = Parser.get_demands_from_file(net_string_demands)

    # for x in range(0, len(list_of_links)):
    #     list_of_links[x].print_link_properties()

    # for y in range(0, len(list_of_demands)):
    #     list_of_demands[y].print_demand_properties()

    for item in generate_first_population(list_of_demands, 6):
        for gene in item.list_of_genes:
            print(gene.list_of_alleles)
