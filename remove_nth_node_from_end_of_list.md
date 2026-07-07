# input
a linked-list head and an integer n

# output
a new linked-list with the original nth node from end removed

# steps
1. two pointers: i and j; i=0 j=n-1
2. move i and j simultaneously until head[j].next is None
3. head[i].next=head[i].next.next (removing the nth node)
4. return head

# requirements
1. write a python function, test it yourself, and put the code into remove_nth_node_from_end_of_list.py
2. start with: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: