# input
integer array nums and integer k(target sum)

# output
an integer(the number of subarrays whose sum is k)

# steps
1. i=j=0 count=0
2. iterate through the array using i and create a dictionary linking sum[0,i] to its value(∑nums[0] to nums[i])
3. iterate through the array using j and see if k-sum[0,j] is in the dictionary; if so, count+=1 (reminder: if k-sum[0,j]=sum[0,i], j>i must be true)
3. return count

# requirements
1. write a python function, test it yourself, and put the code into subarray_sum_equals_k.py
2. start with: def subarraySum(self, nums: List[int], k: int) -> int: