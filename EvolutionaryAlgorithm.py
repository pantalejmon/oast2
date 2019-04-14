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
