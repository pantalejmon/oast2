import unittest

from Parser import *


class TestLinksAndDemands(unittest.TestCase):

    # Open text file, split into 2 parts by -1
    with open(net4_file_path, "r") as net_file:
        # Split file string to 2 strings, each for links and demands
        net_string_links, net_string_demands = net_file.read().split("-1")

    # Test if number of links from file is equal to list of links length
    def test_numbers_of_links(self):
        __number_of_links = get_number_of_links(net_string_links)
        __list_of_links = get_links_list_from_file(net_string_links)
        self.assertEqual(__number_of_links, len(__list_of_links))

    # Test if number of demands from file is equal to list of demands length
    def test_numbers_of_demands(self):
        __number_of_demands = get_number_of_demands(net_string_demands)
        __list_of_demands = get_demands_from_file(net_string_demands)
        self.assertEqual(__number_of_demands, len(__list_of_demands))
