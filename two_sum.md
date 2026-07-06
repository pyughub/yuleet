# input
    integer array nums(length between 2 and 10^4, integer value between -10^9 and 10^9); integer target(between -10^9 and 10^9)

# output
    integer array inds, containing the indexes of the two integers whose sum is target.for every input, only one output exists

# steps
    1. use a double loop. fix one number and its index i and iterate through the numbers to its right.
    2. check the sum of the numbers. if sum==target, return [i,j]; else continue the iteration until you determine the two

# requirements
    1. write a python function and put the code into two_sum.py
    2. start with: def twoSum(self, nums: List[int], target: int) -> List[int]:
    