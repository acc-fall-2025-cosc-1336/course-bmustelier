import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../src/homework/c_decisions'))
from decisions import get_letter_grade, get_options_ratio, get_faculty_rating

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

class TestOptionsRatioAndFacultyRating(unittest.TestCase):
    def test_get_options_ratio(self):
        self.assertAlmostEqual(get_options_ratio(45, 50), 0.9)
        self.assertAlmostEqual(get_options_ratio(40, 50), 0.8)
        self.assertAlmostEqual(get_options_ratio(35, 50), 0.7)
        self.assertAlmostEqual(get_options_ratio(30, 50), 0.6)
        self.assertAlmostEqual(get_options_ratio(25, 50), 0.5)
        self.assertEqual(get_options_ratio(0, 0), 0)

    def test_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating(0.95), "Excellent")
        self.assertEqual(get_faculty_rating(0.9), "Excellent")
        self.assertEqual(get_faculty_rating(0.85), "Very Good")
        self.assertEqual(get_faculty_rating(0.75), "Good")
        self.assertEqual(get_faculty_rating(0.65), "Needs Improvement")
        self.assertEqual(get_faculty_rating(0.59), "Unacceptable")
        self.assertEqual(get_faculty_rating(0), "Unacceptable")
        self.assertEqual(get_faculty_rating(-0.1), "Invalid Ratio")
        self.assertEqual(get_faculty_rating(1.1), "Invalid Ratio")

if __name__ == "__main__":
    unittest.main()