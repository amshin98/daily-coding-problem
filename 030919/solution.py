'''
It's been like 5 months but we're finally back... Going to try to commit myself to doing these everyday, at the very minimum just the solution (or what I think it is). You can't get better at something without practice (perfect practice makes perfect, thanks Coach Mike), so in order to get better at coding this is the least I can do.

-DFS comes to mind
-If it's a tie, just use the first sub_sum
'''

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.sub_sum = self.value

    def __str__(self):
        return "[value: %d left: %d right: %d]" % (self.value, self.left.value, self.right.value)

def first_try(root):
    sums = {"max_key" : None}
    first_try_rec(root, sums)
    return sums["max_key"]

def first_try_rec(cur_node, sums):
    if cur_node.left != None:
        first_try_rec(cur_node.left, sums)
        cur_node.sub_sum += cur_node.left.sub_sum
    if cur_node.right != None:
        first_try_rec(cur_node.right, sums)
        cur_node.sub_sum += cur_node.right.sub_sum
        
    if cur_node.sub_sum in sums:
        sums[cur_node.sub_sum] += 1
    else:
        sums[cur_node.sub_sum] = 1

    if sums["max_key"] == None or sums[cur_node.sub_sum] > sums[sums["max_key"]]:
        
        sums["max_key"] = cur_node.sub_sum