import unittest

from Parser import net4_file_path, net12_1_file_path, net12_2_file_path
from Parser import get_number_of_demands, get_demands_from_file
from EvolutionaryAlgorithm import generate_first_population

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

    # Size of first population should be same as number of demand paths
    def test_size_of_first_population_net4(self):
        __number_of_demand_paths = get_number_of_demands(net4_string_demands)
        __list_of_demands = get_demands_from_file(net4_string_demands)
        __first_population = generate_first_population(__list_of_demands)
        self.assertEqual(__number_of_demand_paths, len(__first_population))

    def test_size_of_first_population_net12_1(self):
        __number_of_demand_paths = get_number_of_demands(net12_1_string_demands)
        __list_of_demands = get_demands_from_file(net12_1_string_demands)
        __first_population = generate_first_population(__list_of_demands)
        self.assertEqual(__number_of_demand_paths, len(__first_population))

    def test_size_of_first_population_net12_2(self):
        __number_of_demand_paths = get_number_of_demands(net12_2_string_demands)
        __list_of_demands = get_demands_from_file(net12_2_string_demands)
        __first_population = generate_first_population(__list_of_demands)
        self.assertEqual(__number_of_demand_paths, len(__first_population))
