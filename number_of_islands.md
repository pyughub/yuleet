# input
a two-dimension grid(array) made of '1's(land) and '0's(water)

# output
an integer(the number of islands)

# steps
1. iterate through the grid. for grid[i][j], if it is '1' and any of the four(or three or two) surrounding elements is '1', then change it to '2'
2. calculate the number of '1's left
3. return the number

# requirements
1. write a python function, test it yourself, and put the code into number_of_islands.py
2. start with: def numIslands(self, grid: List[List[str]]) -> int: