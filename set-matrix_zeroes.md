# input
m x n integer matrix matrix

# output
no output; set rows and columns containing 0 to 0 in-place

# steps
1. rows = [False] * m, cols = [False] * n
2. iterate through the matrix:
    if matrix[i][j] == 0:
        rows[i] = True
        cols[j] = True
3. iterate through the matrix again:
    if rows[i] or cols[j]:
        matrix[i][j] = 0

# steps (O(1) extra space)
1. first_row_zero = any zero in row 0; first_col_zero = any zero in col 0
2. for i in 1..m-1, j in 1..n-1:
    if matrix[i][j] == 0:
        matrix[i][0] = 0
        matrix[0][j] = 0
3. for i in 1..m-1, j in 1..n-1:
    if matrix[i][0] == 0 or matrix[0][j] == 0:
        matrix[i][j] = 0
4. if first_row_zero: zero row 0
5. if first_col_zero: zero col 0

# requirements
1. write a python function, test it yourself, and put the code into set_matrix_zeros.py
2. start with: def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
