import unittest
from python_solution import *

class Tests(unittest.TestCase):
	
	def test_email_example(self):
		numbers = [10, 15, 3, 7]
		sum = 17
		self.assertTrue(basic_solution(numbers, sum))
		self.assertTrue(bonus_solution(numbers, sum))
	
	def test_basic_true_1(self):
		numbers = [12, 10]
		sum = 22
		self.assertTrue(basic_solution(numbers, sum))
		self.assertTrue(bonus_solution(numbers, sum))
	
	def test_basic_true_2(self):
		numbers = [1, 2, 3, 4, 5, 6, 7, 8]
		sum = 9
		self.assertTrue(basic_solution(numbers, sum))
		self.assertTrue(bonus_solution(numbers, sum))
	
	def test_basic_true_3(self):
		numbers = [1, 1]
		sum = 2
		self.assertTrue(basic_solution(numbers, sum))
		self.assertTrue(bonus_solution(numbers, sum))
	
	def test_basic_false_1(self):
		numbers = [12, 15, 6, 1]
		sum = 10
		self.assertFalse(basic_solution(numbers, sum))
		self.assertFalse(bonus_solution(numbers, sum))
	
	def test_basic_false_2(self):
		numbers = [12, 12]
		sum = 25
		self.assertFalse(basic_solution(numbers, sum))
		self.assertFalse(bonus_solution(numbers, sum))
	
	def test_basic_false_3(self):
		numbers = [5, 12]
		sum = 10
		self.assertFalse(basic_solution(numbers, sum))
		self.assertFalse(bonus_solution(numbers, sum))	
		
if __name__ == '__main__':
    unittest.main()