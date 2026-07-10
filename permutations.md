# input
integer array nums (all elements are unique; length between 1 and 6)

# output
an array of integer arrays (all possible permutations of nums; order of the outer array does not matter)

# steps
1. res = [], path = [], used = [False] * len(nums)
2. define backtrack():
   - if len(path) == len(nums): append a copy of path to res, return
   - for each index i from 0 to len(nums) - 1:
     - if used[i], skip
     - mark used[i] = True, append nums[i] to path
     - call backtrack()
     - backtrack: pop path, set used[i] = False
3. call backtrack()
4. return res

# requirements
1. write a python function, test it yourself, and put the code into permutations.py
2. start with: def permute(self, nums: List[int]) -> List[List[int]]:
