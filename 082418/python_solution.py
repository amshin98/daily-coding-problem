'''
Requirements: Passes tests
Performance complexity: O(n^2)
Space complexity: O(1)

Thoughts: Very straightforward solution, first thing that popped into my head
'''
def basic_solution(numbers, sum):
	for x in range(len(numbers) - 1):
		for y in range(x + 1, len(numbers)):
			if numbers[x] + numbers[y] == sum:
				return True;
	return False;
	
'''
Requirements: Passes tests, one pass
Performance complexity: O(n^2)
Space complexity: O(n) (I think)

Thoughts: Technically gets the solution in one pass over numbers
(for each loop) but one could argue that using the the in operator causes
additional passes over counterparts. Plus it only matches the performance
complexity of basic_solution and has higher space complexity
'''
def bonus_solution(numbers, sum):
	counterparts = []
	for number in numbers:
		if number in counterparts:
			return True
		else:
			counterparts.append(sum - number)
	return False