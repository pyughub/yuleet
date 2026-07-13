# input
integer array heights, bar heights in a histogram (width 1 for each bar)

# output
the maximum rectangular area that can be formed in the histogram

# steps
1. use a stack to store indices of bars in increasing height order
2. iterate through heights; when the current bar is lower than the bar at the stack top, pop and compute area using popped height and width
3. width = current index - new stack top - 1 (or current index if stack is empty)
4. push the current index; after the loop, flush remaining bars on the stack the same way
5. return the maximum area seen

# requirements
1. write a python function, test it yourself, and put the code into largest_rectangle_in_histogram.py
2. start with: def largestRectangleArea(self, heights: List[int]) -> int:
