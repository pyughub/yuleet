# input
integer n

# output
all possible valid combinations of parenthesis

# steps
1. there are totally n left parenthesis and n right parenthesis in a combination
2. any combination must start with a left parenthesis; at any place within the combination, the number of right parenthesis before it must not exceed the number of left ones(must be smaller than or equal to)
3. keep track of the total number of left parenthesis filled and unmatched; use backtrack to produce multiple possibilities
4. put all combinations into an array and return it.

# requirements
1. write a python function, test it yourself, and put the code into generate parenthesis.py
2. start with: def generateParenthesis(self, n: int) -> List[str]: