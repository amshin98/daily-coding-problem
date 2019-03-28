'''
So the plan is to do these every morning before class and since they're emailed
at like 9:10 I'll always be a day behind.

Bitwise & to check 1's, then right shift

What about negatives? How many bits does python store integers with? Does it
even matter and should I just fix my loop to match? Will look into this more
later today, time for work.
'''

def first_try(n):
    cur_num = n
    cur_ones = 0
    cur_max = -1
    
    while True:
        if cur_num & 1:
            cur_ones += 1
        elif cur_num & 1 == 0 or cur_num == -1:
            if cur_num == -1:
                cur_ones += 1
            cur_max = max(cur_max, cur_ones)
            cur_ones = 0

        if cur_num <= 0:
            break

        cur_num = cur_num >> 1

    return cur_max