class Node:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


def serialize_helper(cur_node, node_idx, node_list):
   if node_idx >= len(node_list):
      node_list.extend(["EMPTY"] * (len(node_list)))

   node_list[node_idx] = cur_node.val

   if cur_node.left:
      serialize_helper(cur_node.left, node_idx * 2, node_list)
   if cur_node.right:
      serialize_helper(cur_node.right, node_idx * 2 + 1, node_list)


def serialize(root):
   node_list = ["SEN"]

   serialize_helper(root, 1, node_list)

   return " ".join(node_list)


def deserialize(s):
   pass