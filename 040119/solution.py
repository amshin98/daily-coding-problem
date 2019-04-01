'''
BRUH I DELETED 03/26 ON ACCIDENT I THINK. Idk where the solution is, but yeah.
I swear I did it and it worked rip.

We missed the last few days because spring break and Brandon was here,
but now Spring Quarter's here so woop woop.

Haven't really worked with directed graphs before, let's see how this goes
First step is to design the node. Value with adjacency list.

How do we deal with loops? And what about cycles? I'm assuming we don't
have to worry about cycles, since we have to "reverse"..? Nvm shouldn't
be too bad. Don't worry about loops because it's late and we can do this later.
'''

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

def print_trav(root):
    values = [root.value]
    cur_node = root.next_node
    while cur_node.value != None and cur_node.value != root.value:
        values.append(cur_node.value)
        cur_node = cur_node.next

    print(" -> ".join(values))

def first_try():
    return 1