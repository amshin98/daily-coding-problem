import unittest, math
from solution import *

class Tests(unittest.TestCase):

	def tree_builder(self, values):
		nodes = [None]
		for value in values:
			nodes.append(Node(value))

		for i in range(1, math.ceil(len(nodes) / 2)):
			nodes[i].left = nodes[i * 2]
			if i * 2 + 1 < len(nodes):
				nodes[i].right = nodes[i * 2 + 1]
		return nodes[1]

	def test_email_case(self):
		root = self.tree_builder([5, 2, -5])
		self.assertEqual(first_try(root), 2)

	def test_two_leafs(self):
		root = self.tree_builder([2, 11, -20, 24, 50, -100, 50])
		self.assertEqual(first_try(root), 50)


if __name__ == "__main__":
	unittest.main()