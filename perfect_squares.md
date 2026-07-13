# input
an integer n

# output
an integer(the least number of squares we must use to create a sum of n)

# steps
1. make a list of all the square numbers(above 0) below n: sql(arrange in descending order)
2. like an unbounded pack, return min(1+numSquares(n-sql[0]), 1+numSquares(n-sql[1]) all the way to 1+numSquares(n-sql[len(sql)-1]))

# requirements
1. write a python function, test it yourself, and put the code into perfect_squares.py
2. start with: def numSquares(self, n: int) -> int: