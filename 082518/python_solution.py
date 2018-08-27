'''
Requirements: Passes tests
Performance complexity: O(n^2)
Space complexity: O(n)

Thoughts: Not actually the first thing that occurred to me, but since the
follow-up says not to use division, I thought of this for the basic solution.
Had to add a bunch of stuff when I got to the case where 0 was a number
'''
def basic_solution(arr):
	product = 1
	nonzero_product = 1
	for num in arr:
		if num != 0:
			nonzero_product *= num
		product *= num
	ans = []
	for x in range(len(arr)):
		if arr[x] == 0:
			ans.append(nonzero_product)
		elif product == 0:
			ans.append(0)
		else:
			ans.append(product / arr[x])
	return ans
	
'''
Requirements: Passes tests, no division
Performance complexity: O(n^2)
Space complexity: O(n)

Thoughts: The first thing I thought of, not very efficient but it
gets the job done
'''
def bonus_solution(arr):
	ans = []
	product = 1
	for x in range(len(arr)):
		for y in range(len(arr)):
			if y != x:
				product *= arr[y]
		ans.append(product)
		product = 1
	return ans