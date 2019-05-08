import random
from math import ceil

from Models import Gene, Chromosome

# Default values
DEFAULT_MUTATION_PROBABILITY = 0.01
DEFAULT_POPULATION_SIZE = 4
DEFAULT_CROSSOVER_PROBABILITY = 0.10


# Generate first population as List of Chromosomes
def generate_first_population(list_of_demands, population_size_int=DEFAULT_POPULATION_SIZE):
    # Check if provided population size is correct
    if isinstance(population_size_int, int):
        population_size_int = population_size_int
        print("Population size set to: {}".format(population_size_int))
    else:
        population_size_int = DEFAULT_POPULATION_SIZE
        print("Provided incorrect population size, using default value: {}".format(DEFAULT_POPULATION_SIZE))

    first_population_list = list()  # List of Chromosome objects

    # Generate chromosomes number same as provided population size
    for i in range(0, population_size_int):
        first_population_list.append(generate_chromosome(list_of_demands))

    print("First population:")
    return first_population_list


# Generate chromosome from list of Demand objects
def generate_chromosome(list_of_demands):
    list_of_genes = list()  # Empty list for appending Genes
    for item in list_of_demands:
        demand_volume = item.demand_volume  # Get demand volume for current demand
        number_of_demand_paths = item.number_of_demand_paths  # Length of Gene represented by list
        # List of integers for storing alleles of single Gene, initialize it with zeroes
        list_of_alleles = [0] * number_of_demand_paths

        demand_to_assign = demand_volume
        # Randomly assign demand_volume to alleles in Gene
        while demand_to_assign > 0:
            # Choose which allele will be incremented in this loop transition
            allele_to_increment = random.randint(0, number_of_demand_paths - 1)
            # Increment allele value
            list_of_alleles[allele_to_increment] += 1
            # Decrement demand volume left
            demand_to_assign -= 1

        # Add generated Gene to Chromosome
        list_of_genes.append(Gene(list_of_alleles, demand_volume))

    # Create and return chromosome instance
    chromosome = Chromosome(list_of_genes, 0, 0)  # ToDo: implement, calculate and pass fitness
    return chromosome


# Decide and perform mutation on passed chromosome based on mutation
# probability
def mutate_chromosome(chromosome, __mutation_probability=DEFAULT_MUTATION_PROBABILITY):
    # Check if passed probability is in range [0;1]
    if 0 < __mutation_probability <= 1:
        __mutation_probability = __mutation_probability
    else:
        # Passed probability is incorrect, use default value
        __mutation_probability = DEFAULT_MUTATION_PROBABILITY

    for gene in chromosome.list_of_genes:
        # For each gene on the list, decide if mutation will be performed
        if get_random_boolean_based_on_probability(__mutation_probability):
            # Number of Alleles in passed Chromosome
            __number_of_alleles = len(gene.list_of_alleles)

            # Randomly select 2 gene values to mutate
            __first_gene_value_to_swap = random.randint(0, __number_of_alleles - 1)
            __second_gene_value_to_swap = random.randint(0, __number_of_alleles - 1)

            # If allele to decrement = 0, choose another
            while gene.list_of_alleles[__first_gene_value_to_swap] <= 0:
                __first_gene_value_to_swap = random.randint(0, __number_of_alleles - 1)

            # When allele indexes are the same, choose new index for second
            # allele index
            while __second_gene_value_to_swap == __first_gene_value_to_swap:
                __second_gene_value_to_swap = random.randint(0, __number_of_alleles - 1)

            # Shift one unit demand from one gene to another
            gene.list_of_alleles[__first_gene_value_to_swap] -= 1
            gene.list_of_alleles[__second_gene_value_to_swap] += 1    
            return True
        else:
            return False


# Perform crossover, return list with passed chromosomes and offsprings
# ToDo: Best chromosomes should have higher probability to become parents (sort
# list of chromosomes by fitness?)
def crossover_chromosomes(list_of_chromosomes, crossover_probability=DEFAULT_CROSSOVER_PROBABILITY):
    # Check if passed probability is in range [0;1]
    if 0 < crossover_probability <= 1:
        crossover_probability = crossover_probability
    else:
        # Passed probability is incorrect, use default value
        crossover_probability = DEFAULT_CROSSOVER_PROBABILITY

    # Perform crossovers
    list_of_parents_and_offsprings = list()
    # Add all chromosomes from passed list (parents), later we will be adding
    # only the offsprings
    list_of_parents_and_offsprings += list_of_chromosomes

    while len(list_of_chromosomes) >= 2:
        # Take parents from the list
        first_parent_genes = list_of_chromosomes.pop(0).list_of_genes
        second_parent_genes = list_of_chromosomes.pop(0).list_of_genes

        # Determine if crossover happens for each pair of parents
        if get_random_boolean_based_on_probability(crossover_probability):

            first_offspring_genes = list()
            second_offspring_genes = list()

            # Loop through genes and create offsprings
            for i in range(0, len(first_parent_genes)):
                # Decide which gene is taken from which parent
                if get_random_boolean_based_on_probability(0.5):
                    # First offspring gets gene from first parent, second
                    # offspring from second parent
                    first_offspring_genes.append(first_parent_genes[i])
                    second_offspring_genes.append(second_parent_genes[i])
                else:
                    # First offspring gets gene from second parent, second
                    # offspring from first parent
                    first_offspring_genes.append(second_parent_genes[i])
                    second_offspring_genes.append(first_parent_genes[i])

            # Add offsprings to list
            list_of_parents_and_offsprings.append(Chromosome(first_offspring_genes,0,0))  
            list_of_parents_and_offsprings.append(Chromosome(second_offspring_genes,0,0))  

            

    return list_of_parents_and_offsprings


# Calculate and return fitness for passed Chromosome list of genes
def calculate_fitness(links, demands, population):
    for chromosome in population:
        l = [0 for i in range(len(links))]
        y = [0 for i in range(len(links))]
        f = [0 for i in range(len(links))]
        chromosome.fitness_ddap = 0
        chromosome.fitness_dap = 0
        for d in range(len(chromosome.list_of_genes)):
            for p in range(len(chromosome.list_of_genes[d].list_of_alleles)):
                for e in range(len(links)):
                    tmp = chromosome.list_of_genes[d].list_of_alleles[p]
                    if check_link_in_demand(e+1, demands[d], p):
                        l[e] += chromosome.list_of_genes[d].list_of_alleles[p]
        for e in range(len(links)):
            y[e] = ceil(l[e]/links[e].link_module)
            f[e] = l[e] - links[e].number_of_modules*links[e].module_cost
            chromosome.fitness_ddap += y[e] * links[e].module_cost
        chromosome.fitness_dap = max(f)



# Get boolean value based on passed probability [0-1]
def get_random_boolean_based_on_probability(probability):
    return random.random() < probability


# Check if given link is in demand
def check_link_in_demand(link, demand, p):
    path = demand.list_of_demand_paths[p]
    if str(link) in path.link_id_list:
            return True
    else:
        return False   
