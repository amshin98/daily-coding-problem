import os.path
import sys
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from test_utils import *
from solution import *


class Tests(unittest.TestCase):

   def test_given(self):
      tree_2 = BTNode(2)
      tree_4 = BTNode(4)
      tree_5 = BTNode(5)
      tree_3 = BTNode(3, tree_4, tree_5)
      tree_root = BTNode(1, tree_2, tree_3)

      level_wise(tree_root)

   def test_1(self):
      tree_3 = BTNode(3)
      tree_4 = BTNode(4)
      tree_5 = BTNode(5)
      tree_2 = BTNode(2, tree_4, tree_5)
      tree_root = BTNode(1, tree_2, tree_3)

      level_wise(tree_root)

if __name__ == "__main__":
   unittest.main()
