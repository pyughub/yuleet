# input
an m*n matrix

# output
an array consisting of all elements of the matrix in clockwise order

# steps
1. i=j=0 use i,j to keep track of the current position and borders: i<m j<n
2. first increase i until it hits border; then increase j, when j hits border too, backtrack i (now i<m-1 because the first row has been recorded); continue in this way
3. put all the elements in order into an array
4. return the array

# requirements
1. write a python function, test it yourself, and put the code into spiral_matrix.py
2. start with: def spiralOrder(self, matrix: List[List[int]]) -> List[int]: