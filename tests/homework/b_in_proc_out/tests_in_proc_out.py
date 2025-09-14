import unittest
import sys
import os

# Add src directory to sys.path for direct execution
current_dir = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(current_dir, '../../../src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from homework.b_in_proc_out.output import get_number, multiply_numbers

class Test_Config(unittest.TestCase):

    def test_get_number_1(self):
        #test that the function get_number returns 1
        self.assertEqual(1, get_number(1))
    
    def test_get_number_2(self):
        #test that the function get_number returns 2
        self.assertEqual(2, get_number(2))


# Unit tests for multiply_numbers
class Test_MultiplyNumbers(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_multiply_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)

    def test_multiply_negative(self):
        self.assertEqual(multiply_numbers(-2, 6), -12)

    def test_multiply_both_negative(self):
        self.assertEqual(multiply_numbers(-3, -7), 21)


