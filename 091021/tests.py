import unittest
from solution import *

class Tests(unittest.TestCase):

   def test_given(self):
      self.assertEqual(1, find_majority([1, 2, 1, 1, 3, 1, 4, 0, 1]))


   def test_1(self):
      self.assertEqual(0, find_majority([0, 0, 0, 0, 0, 0]))

      
   def test_2(self):
      self.assertEqual(0, find_majority([0, 0, 0, 1, 1, 2, 0]))

      
   def test_3(self):
      self.assertEqual(0, find_majority([0, 0, 0, 1, 1]))

if __name__ == "__main__":
   unittest.main()
