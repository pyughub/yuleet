# input
non-descending integer array nums; integer target

# output
[start index, end index] or [-1,-1](target not in nums)

# steps 
1. use binary search to look for target; if not found, return [-1,-1]
2. use two pointers to determine the start index and end index of target(in case there are multiple targets).
3. return [start index, end index]

# requirements
1. write a python function, test it yourself, and put the code into find_first_and_last_position_of_element_in_sorted_array.py
2. start with: def searchRange(self, nums: List[int], target: int) -> List[int]: