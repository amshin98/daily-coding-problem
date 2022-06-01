'''
Given an array of integers, determine whether it contains a Pythagorean
triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation
a ** 2 + b ** 2 = c ** 2.
'''

def approach_2(ints):
   '''
   Square and sort the list asc. Starting from the leftmost number, designate
   this as c ** 2. From the right side list, pick two numbers that sum up to
   it. Do this by generating a hash table (two sum) and using it.

   O(n ** 2)
   '''
   squared = [x ** 2 for x in ints.sort() if x > 0]

   for i in range(len(squares) - 1):
      # square is c ** 2
      square = squares[i]
      sum_dict = {}
      for j in range(i + 1, len(squares)):
         cur_sq = squares[j]
         if j in sum_dict:
            return True
         else:
            sum_dict[square]

def approach_1(ints):
   '''
   Naive approach. List comprehensions. Square the ints. For each new
   number, generate a new list subtracting that new number from everything else.
   For every subtracted number, check if it exists in the squared list. 
   
   O(n ** 3) :/
   '''
   squared = [x ** 2 for x in ints if x > 0]
   for i in range(len(squared)):
      square = squared[i]
      # square is a ** 2
      subtracted = [x + square for x in squared]
      for j in range(len(subtracted)):
         sub_num = subtracted[j]
         # sub_num is one possible b ** 2 added to an a ** 2 (c ** 2)
         for k in range(len(squared)):
            if sub_num == squared[k] and i != k:
               return True
   return False


def tests(approach):
   ''' Run the tests using the given approach '''
   # < 3 items case
   assert approach([1, 2]) == False

   # 3 items true
   assert approach([3, 4, 5]) == True

   # 3 items false
   assert approach([3, 3, 4]) == False

   # Negative numbers
   assert approach([-3, -4, -5]) == False

   # Zeroes
   assert approach([0, 0, 0]) == False
   
   # Longer lists false
   assert approach([63, 40, 75, 38, 70, 18, 52]) == False
   
   # Longer lists true
   assert approach([63, 3, 40, 75, 4, 38, 70, 18, 5, 52]) == True

   print("Tests passed")
   

if __name__ == '__main__':
   tests(approach_1)