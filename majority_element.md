# input
integer array nums(non-empty; a majority element that appears more than floor(n/2) times always exists)

# output
an integer(the majority element)

# steps
1. init candidate=nums[0], count=0
2. iterate nums: if count==0, set candidate=num; then count+=1 if num==candidate else count-=1
3. return candidate (pairs of different values cancel; majority always remains)

# requirements
1. write a python function, test it yourself, and put the code into majority_element.py
2. start with: def majorityElement(self, nums: List[int]) -> int:
