'''
I'm thinking swapping stuff?
'''

def first_try(array, k):
   for i in range(len(array)):
      tmp = array[i]
      idx = (i + k) % len(array)
      array[i] = array[idx]
      array[idx] = tmp

