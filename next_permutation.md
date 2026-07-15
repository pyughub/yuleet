# input
integer array nums

# output
its next permutation with higher dictionary order

# steps
1. iterate backwards, find the largest k that nums[k]<nums[k+1]
2. temp=nums[k]; do a bubblesort to the subarray made up of nums[k] and those to its right
3. look for temp in the newly arranged subarray and move the element currently to its immediate right to be the first element of the subarray while keeping the rest in order(a series of exchanges)
4. if nums is at highest dictionary order in the first place(completely descending), simply reverse it.

# requirements
1. write a python function, test it yourself, and put the code into next_permutation.py
2. start with: def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """