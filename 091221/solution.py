'''
# First pass, doesn't work for one zero in input
def products(input_list):
   product = 1

   for item in input_list:
      product = product * item

   ans = []

   for item in input_list:
      if item == 0:
         ans.append(0)
      else:
         ans.append(int(product / item))

   return ans
'''

# Second pass, without division, bad efficiency
def products(input_list):
   ans = []

   for i in range(len(input_list)):
      product = 1
      for j in range(len(input_list)):
         if i != j:
            product = product * input_list[j]

      ans.append(product)

   return ans