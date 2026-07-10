# input
integer array candidates(with no repeating elements); integer target

# output
different combinations of numbers whose sum is target, organized as an array

# steps
1. numbers in candidates can be picked repeatedly
2. sort candidates in ascending order
3. go from the first element; temp = target-candidates[0]; if temp>0 then make temp the new target and start again
4. if target==0 after any number is integrated, append the combination into the array to be returned; if target<0, continue to look for other possibilities.
5. use backtrack to look for multiple combinations.

# requirements
1. write a python function, test it yourself, and put the code into combination_sum.py
2. start with: def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: