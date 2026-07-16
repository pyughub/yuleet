# input
integer array nums with n+1 elements(each in [1, n]; exactly one value repeats)

# output
an integer(the duplicated value)

# steps
1. treat nums as a linked list: index i points to nums[i] (duplicate creates a cycle)
2. tortoise moves 1 hop (i=nums[i]), hare moves 2 hops (j=nums[nums[j]]); start i=j=0 until they meet
3. reset i=0; both move 1 hop until they meet again — that node is the cycle entrance (the duplicate)
4. return i

# requirements
1. write a python function, test it yourself, and put the code into find_the_duplicate_number.py
2. start with: def findDuplicate(self, nums: List[int]) -> int:
3. do not modify nums; O(1) extra space
