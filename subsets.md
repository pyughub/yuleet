# input
integer array nums

# output
all subsets of nums

# steps
1. organize by the number of elements in each group of subsets: from 0 to len(nums)
2. for each group, use the backtrack method similar to permutations.py but arrange and search in ascending order so as to ensure all subsets are different
3. integrate all subsets into an array and return the array

# requirements
1. write a python function, test it yourself, and put the code into subsets.py
2. start with: def subsets(self, nums: List[int]) -> List[List[int]]: