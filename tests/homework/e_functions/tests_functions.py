import unittest
from src.homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax

class TestPayrollFunctions(unittest.TestCase):
    def test_gross_pay(self):
        self.assertEqual(get_gross_pay(40, 10), 400)
        self.assertEqual(get_gross_pay(45, 10), 475)
        self.assertEqual(get_gross_pay(30, 10), 300)

    def test_fica_tax(self):
        self.assertEqual(get_fica_tax(400), 30)
        self.assertEqual(get_fica_tax(475), 36)
        self.assertEqual(get_fica_tax(300), 22)

    def test_federal_tax(self):
        self.assertEqual(get_federal_tax(400), 32)
        self.assertEqual(get_federal_tax(475), 38)
        self.assertEqual(get_federal_tax(300), 24)

if __name__ == "__main__":
    unittest.main()