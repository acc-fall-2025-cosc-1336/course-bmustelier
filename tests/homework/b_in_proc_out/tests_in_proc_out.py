import unittest
from src.homework.b_in_proc_out.in_proc_out import multiply_numbers

class Test_MultiplyNumbers(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_multiply_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)

    def test_multiply_negative(self):
        self.assertEqual(multiply_numbers(-2, 6), -12)

    def test_multiply_both_negative(self):
        self.assertEqual(multiply_numbers(-3, -7), 21)


