import random

from Models import Gene, Chromosome

# Default value for mutation probability
DEFAULT_MUTATION_PROBABILITY = 0.01
DEFAULT_POPULATION_SIZE = 4


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
        # ToDo: Implement random generation of Genes for first generation
        list_of_alleles = list()  # List of Int representing alleles in single Gene
        list_of_alleles.append(demand_volume)
        for x in range(1, number_of_demand_paths):
            list_of_alleles.append(0)

        list_of_genes.append(Gene(list_of_alleles, demand_volume))

    # Create and return chromosome instance
    chromosome = Chromosome(list_of_genes, 1)  # ToDo: implement, calculate and pass fitness
    return chromosome


# Decide and perform mutation on passed chromosome based on mutation probability
def mutate_chromosome(chromosome, __mutation_probability=DEFAULT_MUTATION_PROBABILITY):
    # Check if passed probability is in range [0;1]
    if 0 < __mutation_probability <= 1:
        __mutation_probability = __mutation_probability
    else:
        # Passed probability is incorrect, use default value
        __mutation_probability = DEFAULT_MUTATION_PROBABILITY

    # Number of Genes in passed Chromosome
    __number_of_genes = len(chromosome.list_of_genes)

    print("Performing mutation")

    for gene in chromosome.list_of_genes:
        # For each gene on the list, decide if mutation will be performed
        if get_random_boolean_based_on_probability(__mutation_probability):
            # Perform mutation
            # Randomly select 2 gene values to mutate
            __first_gene_value_to_swap = random.randint(0, __number_of_genes)
            __second_gene_value_to_swap = random.randint(0, __number_of_genes)
            # ToDO: handle when selected genes are the same or first is = 0
            if gene.list_of_alleles[__first_gene_value_to_swap] > 0:
                # Shift one unit demand from one gene to another
                gene.list_of_alleles[__first_gene_value_to_swap] -= 1
                gene.list_of_alleles[__second_gene_value_to_swap] += 1
        else:
            return


# Get boolean value based on passed probability [0-1]
def get_random_boolean_based_on_probability(probability):
    return random.random() < probability
