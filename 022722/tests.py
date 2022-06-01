from re import L
import unittest
from solution import *
import random

def preorder(root):
   res = []
   preorder_helper(res, root)
   return res

def preorder_helper(acc, root):
   acc.append(root.data)
   if root.left != None:
      preorder_helper(acc, root.left)
   if root.right != None:
      preorder_helper(acc, root.right)


def inorder(root):
   res = []
   inorder_helper(res, root)
   return res

def inorder_helper(acc, root):
   if root.left != None:
      inorder_helper(acc, root.left)
   acc.append(root.data)
   if root.right != None:
      inorder_helper(acc, root.right)


class Tests(unittest.TestCase):

   def test_email_example(self):
      pre_list = [1, 2, 4, 5, 3, 6, 7]
      in_list = [4, 2, 5, 1, 6, 3, 7]

      res_root = pre_in_to_tree(pre_list, in_list)

      self.assertListEqual(pre_list, preorder(res_root))
      self.assertListEqual(in_list, inorder(res_root))

   def random_test(self, size):
      '''Generate a random BT and run a test on it'''
      nums = random.sample(range(100), size)
      bst = BST()
      for num in nums:
         bst.insert(num)

      pre_list = preorder(bst.root)
      in_list = inorder(bst.root)

      print("Testing for")
      print("Pre", pre_list)
      print("Ino", in_list)

      res_root = pre_in_to_tree(pre_list, in_list)

      self.assertListEqual(pre_list, preorder(res_root))
      self.assertListEqual(in_list, inorder(res_root))

   def test_random_lists(self):
      for i in range(10):
         self.random_test(i + 2 )


if __name__ == "__main__":
   unittest.main()