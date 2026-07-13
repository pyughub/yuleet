# input
integer array nums(with n elements)

# output
integer(the lowest times of jumping to get to nums[n-1])

# steps
1. start from nums[0], look for the first i that fits nums[i]+i=len(nums)-1
2. make num[i] the new goal and redo step1(starting from nums[0], find the first j that makes nums[j]+j=i)
3. keep track of the numbers needed and return the number
4. reminder: i+nums[i]<n

# requirements
1. write a python function, test it yourself, and put the code into jump_game_ii.py
2. start with: def jump(self, nums: List[int]) -> int: