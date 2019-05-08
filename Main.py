import Parser
import random

from EvolutionaryAlgorithm import generate_first_population, mutate_chromosome, crossover_chromosomes, calculate_fitness
from BruteForceAlgorithm import  run_brute_force

# Seed for first use of random functions
DEFAULT_RANDOM_SEED = 7

#Numbers of iterations
MAX_NUMBER_OF_ITERATIONS = 25
MAX_NUMBER_OF_MUTATIONS = 4
MAX_NUMBER_OF_NOT_IMPROVED_ITERATIONS = 10

# Set random seed before first use
random.seed(DEFAULT_RANDOM_SEED)

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
    first_population = generate_first_population(list_of_demands, 4)
    iterations = 0
    mutations = 0
    not_improved_iterations = 0
    current_population = first_population
    calculate_fitness(list_of_links, list_of_demands, current_population)

    for item in first_population:
        print('Genes of current chromosome')
        for gene in item.list_of_genes:
            print(gene.list_of_alleles)
        print("DAP:" + str(item.fitness_dap))
        print("DDAP:" + str(item.fitness_ddap))
	
    while iterations < MAX_NUMBER_OF_ITERATIONS and mutations < MAX_NUMBER_OF_MUTATIONS and not_improved_iterations < MAX_NUMBER_OF_NOT_IMPROVED_ITERATIONS:
        new_population = crossover_chromosomes(current_population, 0.1)
        for chromosome in new_population:
            if mutate_chromosome(chromosome):
                mutations += 1
        calculate_fitness(list_of_links, list_of_demands, new_population)
        current_population = new_population
        iterations += 1

    print("------------ LAST POPULATION --------------")
    for item in current_population:
        print('Genes of current chromosome')
        for gene in item.list_of_genes:
            print(gene.list_of_alleles)
        print("DAP:" + str(item.fitness_dap))
        print("DDAP:" + str(item.fitness_ddap))

    print('\n')
    print("------------ BRUTE FORCE --------------")
    print('\n')

with open(Parser.net4_file_path, "r") as net_file:
#    # Split file string to 2 strings, each for links and demands
    net_string_links, net_string_demands = net_file.read().split("-1")
#    # List for holdings Link objects, get Link objects from txt string
    links = Parser.get_links_list_from_file(net_string_links)
    demands = Parser.get_demands_from_file(net_string_demands)
#    #Zakomentowane bo muli i do poprawy jeszcze
    #run_brute_force(demands,links)
