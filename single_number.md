# input
integer array nums(non-empty; every element appears twice except one that appears once)

# output
an integer(the element that appears only once)

# steps
1. init result=0
2. xor every num into result (a^a=0 and a^0=a, so pairs cancel and the single one remains)
3. return result

# requirements
1. write a python function, test it yourself, and put the code into single_number.py
2. start with: def singleNumber(self, nums: List[int]) -> int:
3. O(n) time and O(1) extra space
