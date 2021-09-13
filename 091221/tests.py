import unittest
from solution import *


class Tests(unittest.TestCase):

   def test_given_1(self):
      self.assertEqual([120, 60, 40, 30, 24], products([1, 2, 3, 4, 5]))

   def test_given_2(self):
      self.assertEqual([2, 3, 6], products([3, 2, 1]))

   def test_zero(self):
      self.assertEqual([36, 0, 0, 0], products([0, 2, 3, 6]))

   def test_zeroes(self):
      self.assertEqual([0, 0, 0, 0], products([0, 2, 3, 0]))

   def test_ones(self):
      self.assertEqual([1, 1, 1, 1, 1, 1], products([1, 1, 1, 1, 1, 1]))

if __name__ == "__main__":
   unittest.main()
