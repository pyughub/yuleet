# input
integer array nums; integer k (>=0)

# output
None(rotate the array on the spot)

# steps
1. iterate through the array: nums[i]=nums[(k+i)%4](original)

# requirements
1. write a python function, test it yourself, and put the code into rotate_array.py
2. start with: def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """