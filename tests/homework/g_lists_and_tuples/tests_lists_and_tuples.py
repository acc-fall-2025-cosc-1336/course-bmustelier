import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../src/homework/g_lists_and_tuples'))
from lists import get_lowest_list_value, get_highest_list_value


class TestLists(unittest.TestCase):
	def test_get_lowest_list_value(self):
		values = [8, 10, 1, 50, 20]
		self.assertEqual(get_lowest_list_value(values), 1)

	def test_get_highest_list_value(self):
		values = [8, 10, 1, 50, 20]
		self.assertEqual(get_highest_list_value(values), 50)


if __name__ == "__main__":
	unittest.main()