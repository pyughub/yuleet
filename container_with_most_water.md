# input
array height

# output
integer maxarea

# steps
1. maxarea = 0 i = 0 j = len(height)
2. while j>i:
    area = (j-i)*min(height[i],height[j])
    if area > maxarea:
        maxarea = area
    if height[i]>height[j]:
        j-=1
    else:
        i+=1
3. return maxarea

# requirements
1. write a python function and put the code into container_with_most_water.py
2. start with: def maxArea(self, height: List[int]) -> int: