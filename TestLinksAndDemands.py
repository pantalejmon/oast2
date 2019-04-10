import unittest

from Parser import net4_file_path, net12_1_file_path, net12_2_file_path
from Parser import get_links_list_from_file, get_demands_from_file, \
    get_number_of_links, get_number_of_demands

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


class TestLinksAndDemands(unittest.TestCase):

    # Test if number of links from net_4 file is equal to list of links length
    def test_numbers_of_links_net4(self):
        __number_of_links_net4 = get_number_of_links(net4_string_links)
        __list_of_links_net4 = get_links_list_from_file(net4_string_links)
        self.assertEqual(__number_of_links_net4, len(__list_of_links_net4))

    # Test if number of demands from net4 file is equal to list of demands length
    def test_numbers_of_demands_net4(self):
        __number_of_demands_net4 = get_number_of_demands(net4_string_demands)
        __list_of_demands_net4 = get_demands_from_file(net4_string_demands)
        self.assertEqual(__number_of_demands_net4, len(__list_of_demands_net4))

    # Test if number of links from net12_1 file is equal to list of links length
    def test_numbers_of_links_net12_1(self):
        __number_of_links_net12_1 = get_number_of_links(net12_1_string_links)
        __list_of_links_net12_1 = get_links_list_from_file(net12_1_string_links)
        self.assertEqual(__number_of_links_net12_1, len(__list_of_links_net12_1))

    # Test if number of demands from net12_1 file is equal to list of demands length
    def test_numbers_of_demands_net12_1(self):
        __number_of_demands_net12_1 = get_number_of_demands(net12_1_string_demands)
        __list_of_demands_net12_1 = get_demands_from_file(net12_1_string_demands)
        self.assertEqual(__number_of_demands_net12_1, len(__list_of_demands_net12_1))

    # Test if number of links from net12_2 file is equal to list of links length
    def test_numbers_of_links_net12_2(self):
        __number_of_links_net12_2 = get_number_of_links(net12_2_string_links)
        __list_of_links_net12_2 = get_links_list_from_file(net12_2_string_links)
        self.assertEqual(__number_of_links_net12_2, len(__list_of_links_net12_2))

    # Test if number of demands from net12_2 file is equal to list of demands length
    def test_numbers_of_demands_net12_2(self):
        __number_of_demands_net12_2 = get_number_of_demands(net12_2_string_demands)
        __list_of_demands_net12_2 = get_demands_from_file(net12_2_string_demands)
        self.assertEqual(__number_of_demands_net12_2, len(__list_of_demands_net12_2))
