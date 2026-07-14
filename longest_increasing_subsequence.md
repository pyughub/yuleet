# input
integer array nums

# output
an integer(the length of the longest strictly increasing subsequence)

# steps
1. use a dp list where dp[i] means the LIS length ending at index i; init all to 1
2. for each i from 1 to n-1, for each j < i: if nums[j] < nums[i], dp[i]=max(dp[i], dp[j]+1)
3. return max(dp)

# requirements
1. write a python function, test it yourself, and put the code into longest_increasing_subsequence.py
2. start with: def lengthOfLIS(self, nums: List[int]) -> int:
