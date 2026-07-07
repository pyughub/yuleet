# input
two non-empty linked-lists l1 and l2 representing two integers(in reversed decimal order)
for example: [2,4,3] represents 342

# output
a linked-list representing their sum, also in reversed decimal order

# steps
1. have two pointers go from both heads at the same time one node at a time
2. calculate (l1[i]+l2[i])*dec; each time i+=1, dec*=10 until one pointer hits None in one of the lists
3. continue with the remaining pointer until it hits None too and calculate in the same way
4. accumulate all the results into one single number and convert it into a reversed linked-list. return the list

# requirements
1. write a python function, test it yourself, and put the code into add_two_numbers.py
2. start with: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 