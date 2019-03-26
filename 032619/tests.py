import unittest
from solution import *

class Tests(unittest.TestCase):

   def test_email_case_1(self):
      self.assertEqual('A', first_try(1))
   def test_email_case_2(self):
      self.assertEqual('AA', first_try(27))

if __name__ == "__main__":
   unittest.main()
