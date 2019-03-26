'''
Aaaaaand we're back after only like 16 days this time go me...
In my defense finals and projects and stuff like that but now that it's break
and spring quarter isn't looking toooo bad hopefully this really does become
a daily thing.

Base 10 to base 26, my favorite
'''

def gen_num_dict():
	num_dict = {}
	
	for i in range(1, 27):
		num_dict[i - 1] = chr(i + 64)

	return num_dict

def first_try(col_num):
	num_dict = gen_num_dict()
	alph_id = []
	div = (col_num - 1) // 26
	rem = (col_num - 1) % 26
	
	while div != 0:
		alph_id.append(num_dict[rem])
		print("rem: %s\n" % rem)
		div = div // 26
		rem = div % 26

	alph_id.append(num_dict[rem])

	alph_id.reverse()
	return "".join(alph_id)