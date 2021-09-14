import unittest
from solution import *


class Tests(unittest.TestCase):

   def test_given(self):
      node = Node('root', Node('left', Node('left.left')), Node('right'))
      self.assertEqual(deserialize(serialize(node)).left.left.val == 'left.left')

if __name__ == "__main__":
   unittest.main()
