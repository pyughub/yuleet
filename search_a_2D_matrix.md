# input
a m*n integer matrix(in ascending order); integer target

# output
boolean value(whether target is in matrix)

# steps
1. iterate through the lines and see which line fits matrix[i][0]<=target<=matrix[i][n-1]
2. within that line, use binary search to look for target. if target in matrix then return true, else return false.

# requirements
1. write a python function, test it yourself, and put the code into search_a_2D_matrix.py
2. start with: def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: