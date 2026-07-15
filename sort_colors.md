# input
integer array nums(each element is 0, 1, or 2)

# output
None(modify nums in-place so colors are ordered 0, then 1, then 2)

# steps
1. init lo=0, mid=0, hi=n-1; maintain nums[0..lo)=0, nums[lo..mid)=1, nums(hi..n-1]=2
2. while mid<=hi: if nums[mid]==0, swap with lo and advance both; if 1, just mid+=1; if 2, swap with hi and hi-=1
3. done when mid>hi (array is partitioned in place)

# requirements
1. write a python function, test it yourself, and put the code into sort_colors.py
2. start with: def sortColors(self, nums: List[int]) -> None:
3. do not use the library built-in sort
