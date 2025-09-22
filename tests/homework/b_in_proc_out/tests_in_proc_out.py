import unittest
from src.homework.b_in_proc_out.output import get_sales_tax_amount, get_tip_amount

class TestBillFunctions(unittest.TestCase):
	def test_get_sales_tax_amount(self):
		self.assertAlmostEqual(get_sales_tax_amount(100), 6.75)
		self.assertAlmostEqual(get_sales_tax_amount(0), 0.0)
		self.assertAlmostEqual(get_sales_tax_amount(50.50), 3.40875)

	def test_get_tip_amount(self):
		self.assertAlmostEqual(get_tip_amount(100, 0.15), 15.0)
		self.assertAlmostEqual(get_tip_amount(80, 0.20), 16.0)
		self.assertAlmostEqual(get_tip_amount(50.50, 0.18), 9.09)

if __name__ == "__main__":
	unittest.main()
