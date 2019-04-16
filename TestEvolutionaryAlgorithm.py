import unittest

from Parser import net4_file_path, net12_1_file_path, net12_2_file_path
from Parser import get_number_of_demands, get_demands_from_file
from EvolutionaryAlgorithm import generate_chromosome, generate_first_population,\
    crossover_chromosomes

# Open net4 text file, split into 2 parts by -1
with open(net4_file_path, "r") as net4_file:
    # Split file string to 2 strings, each for links and demands
    net4_string_links, net4_string_demands = net4_file.read().split("-1")

# Open net12_1 text file, split into 2 parts by -1
with open(net12_1_file_path, "r") as net12_1_file:
    # Split file string to 2 strings, each for links and demands
    net12_1_string_links, net12_1_string_demands = net12_1_file.read().split("-1")

# Open net12_2 text file, split into 2 parts by -1
with open(net12_2_file_path, "r") as net12_2_file:
    # Split file string to 2 strings, each for links and demands
    net12_2_string_links, net12_2_string_demands = net12_2_file.read().split("-1")


class TestEvolutionaryAlgorithm(unittest.TestCase):

    # Size of generated Chromosome should be same as number of demand paths
    def test_size_of_generated_chromosome_list_of_genes_net4(self):
        number_of_demand_paths = get_number_of_demands(net4_string_demands)
        list_of_demands = get_demands_from_file(net4_string_demands)
        chromosome = generate_chromosome(list_of_demands)
        self.assertEqual(number_of_demand_paths, len(chromosome.list_of_genes))

    def test_size_of_generated_chromosome_list_of_genes_net12_1(self):
        number_of_demand_paths = get_number_of_demands(net12_1_string_demands)
        list_of_demands = get_demands_from_file(net12_1_string_demands)
        chromosome = generate_chromosome(list_of_demands)
        self.assertEqual(number_of_demand_paths, len(chromosome.list_of_genes))

    def test_size_of_generated_chromosome_list_of_genes_net12_2(self):
        number_of_demand_paths = get_number_of_demands(net12_2_string_demands)
        list_of_demands = get_demands_from_file(net12_2_string_demands)
        chromosome = generate_chromosome(list_of_demands)
        self.assertEqual(number_of_demand_paths, len(chromosome.list_of_genes))

    # Test if sum of demands on in each gene in Chromosome is the same as demand volume
    def test_demand_volumes_on_chromosome_list_of_genes_net4(self):
        list_of_demands = get_demands_from_file(net4_string_demands)
        first_population = generate_first_population(list_of_demands)
        for chromosome in first_population:
            for gene in chromosome.list_of_genes:
                self.assertEqual(gene.demand_volume, sum(gene.list_of_alleles))

    def test_demand_volumes_on_chromosome_list_of_genes_net12_1(self):
        list_of_demands = get_demands_from_file(net12_1_string_demands)
        first_population = generate_first_population(list_of_demands)
        for chromosome in first_population:
            for gene in chromosome.list_of_genes:
                self.assertEqual(gene.demand_volume, sum(gene.list_of_alleles))

    def test_demand_volumes_on_chromosome_list_of_genes_net12_2(self):
        list_of_demands = get_demands_from_file(net12_2_string_demands)
        first_population = generate_first_population(list_of_demands)
        for chromosome in first_population:
            for gene in chromosome.list_of_genes:
                self.assertEqual(gene.demand_volume, sum(gene.list_of_alleles))

    # Check if new population after crossovers has correct size
    def test_population_size_after_crossover_net4(self):
        list_of_demands = get_demands_from_file(net4_string_demands)
        first_population = generate_first_population(list_of_demands)
        first_population_length = len(first_population)
        new_population = crossover_chromosomes(first_population)
        if len(first_population) % 2 == 0:
            self.assertEqual(first_population_length * 2, len(new_population))
        else:
            self.assertEqual(first_population_length * 2 - 1, len(new_population))

    def test_population_size_after_crossover_net12_1(self):
        list_of_demands = get_demands_from_file(net12_1_string_demands)
        first_population = generate_first_population(list_of_demands)
        first_population_length = len(first_population)
        new_population = crossover_chromosomes(first_population)
        if len(first_population) % 2 == 0:
            self.assertEqual(first_population_length * 2, len(new_population))
        else:
            self.assertEqual(first_population_length * 2 - 1, len(new_population))

    def test_population_size_after_crossover_net12_2(self):
        list_of_demands = get_demands_from_file(net12_2_string_demands)
        first_population = generate_first_population(list_of_demands)
        first_population_length = len(first_population)
        new_population = crossover_chromosomes(first_population)
        if len(first_population) % 2 == 0:
            self.assertEqual(first_population_length * 2, len(new_population))
        else:
            self.assertEqual(first_population_length * 2 - 1, len(new_population))
