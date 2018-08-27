import unittest
from python_solution import *

class Tests(unittest.TestCase):
	
	def test_email_example_1(self):
		arr = [1, 2, 3, 4, 5]
		ans = [120, 60, 40, 30, 24]
		self.assertSequenceEqual(ans, basic_solution(arr))
		self.assertSequenceEqual(ans, bonus_solution(arr))

	def test_email_example_2(self):
		arr = [3, 2, 1]
		ans = [2, 3, 6]
		self.assertSequenceEqual(ans, basic_solution(arr))
		self.assertSequenceEqual(ans, bonus_solution(arr))
	
	def test_basic_1(self):
		arr = [0, 1, 2, 3]
		ans = [6, 0, 0, 0]
		self.assertSequenceEqual(ans, basic_solution(arr))
		self.assertSequenceEqual(ans, bonus_solution(arr))
	
	def test_basic_2(self):
		ans = [1, 1, 1]
		arr = [1, 1, 1]
		self.assertSequenceEqual(ans, basic_solution(arr))
		self.assertSequenceEqual(ans, bonus_solution(arr))
	
if __name__ == '__main__':
    unittest.main()