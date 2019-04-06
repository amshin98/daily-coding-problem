import unittest
from solution import *

class Tests(unittest.TestCase):

    def test_email_case(self):
        test_list = [1, 2, 3, 10]
        self.assertEqual(7, first_try(test_list))

    def test_1(self):
        test_list = [2]
        self.assertEqual(1, first_try(test_list))

    def test_2(self):
        test_list = [1, 3, 4]
        self.assertEqual(2, first_try(test_list))

    def test_3(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(16, first_try(test_list))


if __name__ == "__main__":
   unittest.main()
