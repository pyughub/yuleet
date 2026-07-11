# input
sorted array nums, integer target

# output
index of target in nums; if target is not in nums, the index where it would be inserted in order

# steps
1. set left and right pointers to the start and end of nums
2. while left <= right, pick mid; if nums[mid] equals target, return mid
3. if nums[mid] < target, search the right half (left = mid + 1); otherwise search the left half (right = mid - 1)
4. when the loop ends, return left as the insert position

# requirements
1. write a python function, test it yourself, and put the code into search_insert_position.py
2. start with: def searchInsert(self, nums: List[int], target: int) -> int:
