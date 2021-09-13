'''
Some testing utilities for my DCP stuff
'''

class BTNode:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right

   def __str__(self):
      return "Data: %s" % (self.data)


class BST:
   def __init__(self, root = None):
      self.root = root

   def add_helper(self, cur_node, new_node):
      if new_node.data <= cur_node.data:
         if cur_node.left is None:
            cur_node.left = new_node
         else:
            self.add_helper(cur_node.left, new_node)
      else:
         if cur_node.right is None:
            cur_node.right = new_node
         else:
            self.add_helper(cur_node.right, new_node)

   def add(self, node):
      """Equal to left"""
      if self.root is None:
         self.root = node
      else:
         self.add_helper(self.root, node)

   def print_preorder(self):
      preorder_helper(self.root)

   def preorder_helper(cur_node):
      """TODO: make this work for non-print as well"""

      print(cur_node)
      if cur_node.left != None:
         preorder_helper(cur_node.left)
      if cur_node.right != None:
         preorder_helper(cur_node.right)


def build_BST(items):
   """Build a BST given a list of items to add"""
   tree = BST()

   for item in items:
      tree.add(BTNode(item))

   return tree


class GNode:
   def __init__(self, data, adj_list = None):
      self.data = data
      self.adj_list = adj_list
