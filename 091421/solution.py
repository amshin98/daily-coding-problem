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


def deserialize_helper(cur_idx, val_list):
   left_child = None
   right_child = None

   if len(val_list) > cur_idx * 2 and val_list[cur_idx * 2] != "EMPTY":
      left_child = deserialize_helper(cur_idx * 2, val_list)
   if len(val_list) > cur_idx * 2 + 1 and val_list[cur_idx * 2 + 1] != "EMPTY":
      right_child = deserialize_helper(cur_idx * 2 + 1, val_list)

   return Node(val_list[cur_idx], left_child, right_child)


def deserialize(s):
   val_list = s.split(" ")

   root = deserialize_helper(1, val_list)

   return root