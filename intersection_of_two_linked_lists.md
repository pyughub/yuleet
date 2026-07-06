# input
the first node of two linked-lists, headA and headB

# output
the intersection of the two linked-lists; null if the two linked-lists have no intersection

# steps
1. start from both ends and see if the value matches. if so, continue until the values diverge(become different)
2. return the final one with the same self.next(meaning that they point to the same node instead of the same value)

# requirements
1. write a python function, test it yourself, and put the code into intersection_of_two_linked_lists.py
2. start with: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: