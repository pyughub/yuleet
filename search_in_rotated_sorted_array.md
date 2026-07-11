# input
rotated array nums, originally in ascending order; integer target

# output
boolean value(whether target is in nums)

# steps
1. make sure target is between nums.max and nums.min
2. map nums[i] to its index
2. if target>=nums[0] then do binary search in range(nums[0], nums[max.index]); else do binary search in range(nums[max.index+1], nums[len(nums-1)]) 

# requirements
1. write a python function, test it yourself, and put the code into search_in_rotated_sorted_array.py
2. start with: def search(self, nums: List[int], target: int) -> int: