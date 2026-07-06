# input
integer array nums

# output
an integer(the sum of the maximum subarray)

# steps
1. i=0; iterate through nums, calculate all sum[0,i](∑nums[0] to nums[i])
2. return max of sum[0,i]s - min of sum[0,i]s

# requirements
1. write a python function, test it yourself, and put the code into maximum_subarray.py
2. start with:def maxSubArray(self, nums: List[int]) -> int: