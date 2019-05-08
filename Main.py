import Parser
import random
import time

from EvolutionaryAlgorithm import generate_first_population, mutate_chromosome, crossover_chromosomes, calculate_fitness
from BruteForceAlgorithm import  run_brute_force

# Seed for first use of random functions
DEFAULT_RANDOM_SEED = 7

#Numbers of iterations
MAX_TIME_ELAPSED = 0
MAX_NUMBER_OF_ITERATIONS = 0
MAX_NUMBER_OF_MUTATIONS = 0
MAX_NUMBER_OF_NOT_IMPROVED_ITERATIONS = 0
time_elapsed = 0 
iterations = 0
mutations = 0
not_improved_iterations = 0
# Set random seed before first use
random.seed(DEFAULT_RANDOM_SEED)

filepath = ''
while True:
    x = input("Choose net file. 1.net4 2.net12_1 3.net12_2:     ")
    if x=="1":
        filepath = Parser.net4_file_path
        break
    elif x=="2":
        filepath = Parser.net12_1_file_path
        break
    elif x=="3":
        filepath = Parser.net12_2_file_path
        break
    else:
        print("Wrong choice!")

initial_population_size = int(input("Initial population size:   "))
cross_prob = float(input("Crossover probability:   "))
mut_prob = float(input("Mutation probability:   "))
stop_criterium = " "
while True:
    stop_criterium = input("Choose stop criterium. 1.Duration 2.Number of iterations 3.Number of mutations 4.Not improved since N iterations:     ")
    if stop_criterium=="1":
        MAX_TIME_ELAPSED = int(input("How many seconds?:     "))
        break
    elif stop_criterium=="2":
        MAX_NUMBER_OF_ITERATIONS = int(input("How many iterations?:     "))
        break
    elif stop_criterium=="3":
        MAX_NUMBER_OF_MUTATIONS = int(input("How many mutations:     "))
        break    
    elif stop_criterium=="4":
        MAX_NUMBER_OF_NOT_IMPROVED_ITERATIONS = int(input("N=     "))
        break
    else:
        print("Wrong choice!")

def check_if_stop():
    if stop_criterium=="1":
        return time_elapsed < MAX_TIME_ELAPSED
    elif stop_criterium=="2":
        return iterations < MAX_NUMBER_OF_ITERATIONS
    elif stop_criterium=="3":
        return mutations < MAX_NUMBER_OF_MUTATIONS
    elif stop_criterium=="4":
        return not_improved_iterations < MAX_NUMBER_OF_NOT_IMPROVED_ITERATIONS
    else:
        return False

with open(filepath, "r") as net_file:
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


    first_population = generate_first_population(list_of_demands, initial_population_size)
    
    current_population = first_population
    calculate_fitness(list_of_links, list_of_demands, current_population)

    for item in first_population:
        print('Genes of current chromosome')
        for gene in item.list_of_genes:
            print(gene.list_of_alleles)
        print("DAP:" + str(item.fitness_dap))
        print("DDAP:" + str(item.fitness_ddap))
	
    while check_if_stop():
        start = time.time()
        old_ddap = current_population[0].fitness_ddap
        old_dap = current_population[0].fitness_dap
        new_population = crossover_chromosomes(current_population, cross_prob)
        for chromosome in new_population:
            if mutate_chromosome(chromosome, mut_prob):
                mutations += 1
        calculate_fitness(list_of_links, list_of_demands, new_population)
        new_population.sort(key=lambda x: x.fitness_ddap, reverse=False)
        if  old_ddap >= new_population[1].fitness_ddap and old_dap >= new_population[1].fitness_dap:
            not_improved_iterations += 1
        sliced_population = new_population[:initial_population_size]
        current_population = sliced_population
        end = time.time()
        iterations += 1
        time_elapsed += end - start

    print("iterations:" + str(iterations))
    print("mutations:" + str(mutations))
    print("time elapsed:" + str(time_elapsed))
    
    print("------------ LAST POPULATION BEST CHROMOSOME--------------")
    print('Genes of current chromosome')
    for gene in current_population[0].list_of_genes:
        print(gene.list_of_alleles)
    print("DAP:" + str(current_population[0].fitness_dap))
    print("DDAP:" + str(current_population[0].fitness_ddap))

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
    run_brute_force(demands,links)


