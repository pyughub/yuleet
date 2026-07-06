# input
an array of intervals [start,end]

# output
a new array of intervals with no overlap

# steps
1. sort the intervals according to start[i] in ascending order 
2. iterate through the array; if end[i]>=start[i+1]: merge the two intervals
3. return the new array

# requirements
1. write a python function, test it yourself, and put the code into .py
2. start with: