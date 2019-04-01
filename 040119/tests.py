import unittest
from solution import *

class Tests(unittest.TestCase):

    def email_case(self):
        self.assertEqual(3, first_try(156))

    def test_1(self):
        self.assertEqual(1, first_try(21))

    def test_2(self):
        # NO WORK
        self.assertEqual(2, first_try(-3))


if __name__ == "__main__":
   unittest.main()
