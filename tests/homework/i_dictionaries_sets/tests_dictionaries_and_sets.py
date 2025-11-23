#import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory


class Test_Config(unittest.TestCase):

	def test_add_inventory(self):
		inventory = {}
		# add Widget1 with quantity 10 -> should be 10
		add_inventory(inventory, 'Widget1', 10)
		self.assertIn('Widget1', inventory)
		self.assertEqual(inventory['Widget1'], 10)

		# add Widget1 with quantity 25 -> total should be 35
		add_inventory(inventory, 'Widget1', 25)
		self.assertEqual(inventory['Widget1'], 35)

		# add Widget1 with quantity -10 -> total should be 25
		add_inventory(inventory, 'Widget1', -10)
		self.assertEqual(inventory['Widget1'], 25)


if __name__ == '__main__':
	unittest.main()