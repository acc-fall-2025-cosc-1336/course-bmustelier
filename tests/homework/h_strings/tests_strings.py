import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../src/homework/h_strings'))
from strings import get_hamming_distance, get_dna_complement


class Test_Config(unittest.TestCase):

	def test_get_hamming_distance(self):
		s1 = 'GAGCCTACTAACGGGAT'
		s2 = 'CATCGTAATGACGGCCT'
		self.assertEqual(get_hamming_distance(s1, s2), 7)

	def test_get_dna_complement(self):
		self.assertEqual(get_dna_complement('AAAACCCGGT'), 'ACCGGGTTTT')
