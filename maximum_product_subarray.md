# input
integer array nums

# output
an integer(the product of the maximum product subarray)

# steps
1. keep max_ending and min_ending: the max/min product of subarrays ending at current index
2. for each num, candidates are (num, max_ending*num, min_ending*num); update max_ending=max(candidates), min_ending=min(candidates)
3. track result=max(result, max_ending); return result

# requirements
1. write a python function, test it yourself, and put the code into maximum_product_subarray.py
2. start with: def maxProduct(self, nums: List[int]) -> int:
