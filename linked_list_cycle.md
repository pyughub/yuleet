# input
first node of a linked-list: head

# output
boolean value; if cycle exists the true else false

# steps
1. go down the list and memorise all the nodes visited
2. for each node, see if node.next has been visited; if so then return true.
3. if no such node exists then return false.

# requirements
1. write a python function, test it yourself, and put the code into linked_list_cycle.py
2. start with: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: