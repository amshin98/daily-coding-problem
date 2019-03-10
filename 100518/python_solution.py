'''
Requirements: Passes tests, all methods constant time
Performance complexity: All methods O(1)
Space complexity: O(n)

Thoughts: Shoutout to Tim Kearns and Don Allen for teaching me data structures.
Keep track of the largest and second largest items in the stack as they are
added/removed so we don't have to worry about traversing the stack when max()
is called.
'''

class MyStack:

	first_largest = None
	second_largest = None
	my_stack = []

	def push(val):
		#Check for new largest number
		if val > largest:
			second_largest = largest
			largest = val

		#Append val to our stack
		my_stack.append(val)

	def pop():
