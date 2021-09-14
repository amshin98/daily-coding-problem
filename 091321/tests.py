import unittest
from solution import *


class Tests(unittest.TestCase):

   def test_1(self):
      self.assertEqual([120, 60, 40, 30, 24], products([1, 2, 3, 4, 5]))

if __name__ == "__main__":
   unittest.main()
