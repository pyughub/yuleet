# input
non-negative integer numRows

# output
list of integer lists (the first numRows rows of Pascal's triangle)

# steps
1. use dynamic programming: dp[i][j] is the value at row i, column j
2. base case: dp[i][0] = dp[i][i] = 1 for every row i
3. transition: dp[i][j] = dp[i-1][j-1] + dp[i-1][j] for 0 < j < i
4. build rows from top to bottom and return all rows
5. reminder: row i has i + 1 elements; each number equals the sum of the numbers above-left and above-right

# requirements
1. write a python function, test it yourself, and put the code into Pascal_Triangle.py
2. start with: def generate(self, numRows: int) -> List[List[int]]:
