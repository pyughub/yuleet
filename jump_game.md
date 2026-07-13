# input
an integer array nums

# output
boolean value(whether it is possible to jump to the final element)

# steps
1. create another array dest; dest[i]=nums[i]+i
2. if dest.max>=num[len(nums)-1] then return True else False

# requirements
1. write a python function, test it yourself, and put the code into jump_game.py
2. start with: def canJump(self, nums: List[int]) -> bool: