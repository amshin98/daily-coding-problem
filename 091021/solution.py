from math import floor

def find_majority(input_list):
	majority_count = floor(len(input_list) / 2.0)
	frequencies = {}

	for item in input_list:
		if item not in frequencies:
			frequencies[item] = 1
		else:
			frequencies[item] += 1

		if frequencies[item] > majority_count:
			return item
