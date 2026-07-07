# input
a linked-list head

# output
a swapped linked-list

# steps
1. temp=head.next.next; head.next.next=head; head.next=temp
2. after swapping the first pair in step 1, see the third node as the new head and repeat step 1. always check if there were at least two nodes left unswapped; if there was only one or none left, stop
3. return the head node of the new list.

# requirements
1. write a python function, test it yourself, and put the code into swap_nodes_in_pairs.py
2. start with: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]: