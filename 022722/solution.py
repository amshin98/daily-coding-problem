'''
preorder: N L R
inorder: L N R

- The first thing pre shows is the first node
- How do you know if it's a right child?
- Preorder lists the left branch of the tree
  until it lists some right child (if it exists)
- The first thing in shows is the leftmost child
- Second thing in the in list is the first node with a right
  child, then comes the right child

left arm good, how to determine right arm and children

thought: if pre_list == in_list, right arm only
thought: if pre_list == reverse(in_list), left arm only

trees are made of trees.
left part of in list is left subtree of a node, right is right etc.
left child is the thing after a node in preorder, right child????

the middle of each inorder traversal is the root? No idts. think just right arm

the first thing from the inorder subtree that shows up in the pre tree is
the root?

should be able to split the preorder list. yeah, once we identify the right child
of the root, everything from that node to the right is in the right subtree

1) identify root of subtree
  - first element of preorder list

2) identify new inorder subtrees
  - left and right sides of the root in the inorder list

3) identify new preorder subtrees
  - first appearance of a right inorder list element in the preorder list
  is the start of the right pre sublist, and the rest minus the cur
  root is the left pre sublist


'''

class Node:
   def __init__(self, data, left, right):
      self.data = data
      self.left = left
      self.right = right

   def __repr__(self):
      return "data: %s left: %s right: %s" % (self.data, self.left.data if self.left else None, self.right.data if self.right else None)
   
def pre_in_to_tree(preorder, inorder):

   # If either list is empty, return None
   if len(preorder) == 0:
      return None

   # Find root value
   root_val = preorder[0]

   # If the lists have one element, return the node with None L/R
   if len(preorder) == 1:
      return Node(root_val, None, None)

   # Identify left and right inorder lists
   in_split = inorder.index(root_val)
   left_in = inorder[:in_split]
   right_in = inorder[in_split + 1:] if in_split < len(inorder) - 1 else []

   # Identify left and right preorder lists
   pre_split = 0
   for i in range(1, len(preorder)):
      if preorder[i] in right_in:
         pre_split = i
         break
   
   left_pre = preorder[1:pre_split] if len(preorder) > 1 else []  
   right_pre = preorder[pre_split:] if pre_split < len(preorder) else []

   # Recurse over the left and right subtrees
   left_tree = pre_in_to_tree(left_pre, left_in)
   right_tree = pre_in_to_tree(right_pre, right_in)
   node = Node(root_val, left_tree, right_tree)

   return node

# Test from email
if __name__ == "__main__":
      
   pre_list = [1, 2, 4, 5, 3, 6, 7]
   in_list = [4, 2, 5, 1, 6, 3, 7]

   res_root = pre_in_to_tree(pre_list, in_list)

   print(res_root.data)

   def preorder(acc, root):
      acc.append(root.data)

      if root.left != None:
         preorder(acc, root.left)

      if root.right != None:
         preorder(acc, root.right)


   def inorder(acc, root):
      if root.left != None:
         inorder(acc, root.left)

      acc.append(root.data)

      if root.right != None:
         inorder(acc, root.right)

   test_pre = []
   preorder(test_pre, res_root)
   test_in = []
   inorder(test_in, res_root)

   print("ans")
   print(test_pre)
   print(test_in)