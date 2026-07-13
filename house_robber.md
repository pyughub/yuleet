# input
integer array nums(representing the number of money in each house)

# output
an integer, the maximum number of money that can be stolen

# steps
1. use a dp list
2. for each number, dp[i]=max(dp[i+1], nums[i]+dp[i+2]), i in range(len(nums)-1)
3. return dp[0]

# requirements
1. write a python function, test it yourself, and put the code into house_robber.py
2. start with: def rob(self, nums: List[int]) -> int: