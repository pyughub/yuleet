# input
array nums(length between 1 and 10^4; numbers between -2^31 and 2^31-1)

# output
no output; just rearranging the array on the spot

# steps
1.  nonzero=0
2. for j in range(len(nums)):
    if nums[j] != 0:
        nums[nonzero]=nums[j]
        nonzero+=1
3. for i in range(nonzero, len(nums)):
    nums[i]=0
    
# requirements
1. write a python function and put the code into move_zeroes.py
2. start with: def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """