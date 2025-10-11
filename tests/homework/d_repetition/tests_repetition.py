import unittest

from src.homework.d_repetition.repetition import get_factorial

from src.homework.d_repetition.repetition import sum_odd_numbers


class Test_Config(unittest.TestCase):
    class TestRepetitionFunctions(unittest.TestCase):
        def test_get_factorial(self):
            self.assertEqual(get_factorial(0), 1)
            self.assertEqual(get_factorial(1), 1)
            self.assertEqual(get_factorial(5), 120)
            self.assertEqual(get_factorial(7), 5040)

        def test_sum_odd_numbers(self):
            self.assertEqual(sum_odd_numbers(0), 0)
            self.assertEqual(sum_odd_numbers(1), 1)
            self.assertEqual(sum_odd_numbers(5), 9)   # 1+3+5
            self.assertEqual(sum_odd_numbers(10), 25) # 1+3+5+7+9

if __name__ == "__main__":
    unittest.main()