'''
I'm thinking swapping stuff? Will finish tomorrow
'''

def first_try(array, k):
   for i in range(len(array)):
      idx = (i + k) % len(array)
      tmp = array[idx]
      array[idx] = array[i]
      print(array[i])
      print(idx)
      array[i] = tmp

