import unittest
from solution import *

class Tests(unittest.TestCase):

   def test_one(self):
      arr = [1, 2, 3, 4]
      first_try(arr, 2)
      assertEqual(arr, [3, 4, 1, 2])

if __name__ == "__main__":
   unittest.main()
