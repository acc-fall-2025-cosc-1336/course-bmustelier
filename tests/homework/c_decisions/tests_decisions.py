import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../src/homework/c_decisions'))
from decisions import get_letter_grade

class TestLetterGrade(unittest.TestCase):
    def test_get_letter_grade_A(self):
        self.assertEqual(get_letter_grade(95), 'A')

    def test_get_letter_grade_B(self):
        self.assertEqual(get_letter_grade(85), 'B')

    def test_get_letter_grade_C(self):
        self.assertEqual(get_letter_grade(75), 'C')

    def test_get_letter_grade_D(self):
        self.assertEqual(get_letter_grade(65), 'D')

    def test_get_letter_grade_F(self):
        self.assertEqual(get_letter_grade(50), 'F')

if __name__ == "__main__":
    unittest.main()