'''
Some testing utilities for my DCP stuff
'''

class BSTNode:
   def __init__(self, data, left: BSTNode = None, right: BSTNode = None):
      self.data = data
      self.left = left
      self.right = right

   def __str__(self):
      return "Data: %s Left: %s Right: %s" % (data, left.data, right.data)

class BST:
   def __init__(self, root: BSTNode = None):
      self.root = root

   def add(self, node: BSTNode):
      """Equal to left"""
      add_helper(self.root, node)

   def add_helper(cur_node, new_node):
      if new_node.data < cur_node.data:
         if cur_node.left == None:
            cur_node.left = new_node
         else:
            add_helper(cur_node.left, new_node)
      else:
         if cur_node.right = None:
            cur_node.right = new_node
         else:
            add_helper(cur_node.right, new_node)

   def print_preorder(self):
      preorder_helper(self.root)

   def preorder_helper(cur_node):
      """TODO: make this work for non-print as well"""

      print(cur_node)
      if cur_node.left != None:
         preorder_helper(cur_node.left)
      if cur_node.right != None:
         preorder_helper(cur_node.right)


class GNode:
   def __init__(self, data, adj_list: List[GNode] = None):
      self.data = data
      self.adj_list = adj_list

def build_BST(items):
   """Build a BST given a list of items to add"""
