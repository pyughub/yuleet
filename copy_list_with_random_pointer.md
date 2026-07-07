# input
a linked-list(head) with n nodes, each featuring an extra pointer random

# output
a deep copy of the list

# steps
1. use a dictionary to keep track of the link between nodes
2. construct the new list according to the dictionary
3. return the copied list.

# requirements
1. write a python function, test it yourself, and put the code into copy_list_with_random_pointer.py
2. start with: """
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':