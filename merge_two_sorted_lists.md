# input
2 linked-lists in ascending order

# output
1 merged list in ascending order

# steps
1. go through the two lists and use a dictionary to memorize how many times each value appeared
2. make a new list in ascending order according to the dictionary
3. return the new merged list

# requirements
1. write a python function, test it yourself, and put the code into merge_two_sorted_lists.py
2. start with: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: