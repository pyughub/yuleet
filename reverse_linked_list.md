# input
first node of a linked-list: head

# output
a reversed linked-list

# steps
1. exchange head with head.next; 
2. see head.next->head as a new linked-list and exchange it with the original next of head.next
3. go on until the whole linked-list is reversed.
4. return the reversed linked-list.

# requirements
1. write a python function, test it yourself, and put the code into reverse_linked_list.py
2. start with: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: