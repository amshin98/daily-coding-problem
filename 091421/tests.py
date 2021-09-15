import unittest
from solution import *


class Tests(unittest.TestCase):

   def test_given_tree(self):
      node = Node('root', Node('left', Node('left.left')), Node('right'))
      self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')

      self.assertEqual(deserialize(serialize(node)).left.val, 'left')
      self.assertEqual(deserialize(serialize(node)).right.val, 'right')

      self.assertIsNone(deserialize(serialize(node)).left.left.left)
      self.assertIsNone(deserialize(serialize(node)).right.left)
      self.assertIsNone(deserialize(serialize(node)).right.right)


   def test_only_root(self):
      node = Node('root')
      self.assertEqual(deserialize(serialize(node)).val, 'root')


   def test_only_left(self):
      node = Node('0', Node('1', Node('2', Node('3'))))

      self.assertEqual(deserialize(serialize(node)).val, '0')
      self.assertEqual(deserialize(serialize(node)).left.val, '1')
      self.assertEqual(deserialize(serialize(node)).left.left.val, '2')
      self.assertEqual(deserialize(serialize(node)).left.left.left.val, '3')


   def test_only_right(self):
      node = Node('0', None, Node('1', None, Node('2', None, Node('3'))))

      self.assertEqual(deserialize(serialize(node)).val, '0')
      self.assertEqual(deserialize(serialize(node)).right.val, '1')
      self.assertEqual(deserialize(serialize(node)).right.right.val, '2')
      self.assertEqual(deserialize(serialize(node)).right.right.right.val, '3')

if __name__ == "__main__":
   unittest.main()
