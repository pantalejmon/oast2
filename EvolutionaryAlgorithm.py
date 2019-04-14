import random


# Generate first population from list of Demand objects
def generate_first_population(__list_of_demands):
    list_of_genes = list()  # Chromosome - empty list for appending Genes
    for item in __list_of_demands:
        __demand_volume = item.demand_volume  # Get demand volume for current demand
        __number_of_demand_paths = item.number_of_demand_paths  # Length of Gene represented by list
        # ToDo: Implement random generation of Genes for first generation
        gene = list()
        gene.append(__demand_volume)
        for x in range(1, __number_of_demand_paths):
            gene.append(0)

        list_of_genes.append(gene)

    return list_of_genes


# Decide and perform mutation on passed chromosome based on mutation probability
def mutate_chromosome(__list_of_genes, __mutation_probability=0.01):
    # ToDo: Handle passing probability incorrect range
    __number_of_genes = len(__list_of_genes)

    for gene in __list_of_genes:
        # For each gene on the list, decide if mutation will be performed
        if get_random_boolean_based_on_probability(__mutation_probability):
            # Perform mutation
            # Randomly select 2 gene values to mutate
            __first_gene_value_to_swap = random.randint(0, __number_of_genes)
            __second_gene_value_to_swap = random.randint(0, __number_of_genes)
            # ToDO: handle when selected genes are the same or first is = 0
            if gene[__first_gene_value_to_swap] > 0:
                # Shift one unit demand from one gene to another
                gene[__first_gene_value_to_swap] -= 1
                gene[__second_gene_value_to_swap] += 1
        else:
            return


# Get boolean value based on passed probability [0-1]
def get_random_boolean_based_on_probability(probability):
    return random.random() < probability
