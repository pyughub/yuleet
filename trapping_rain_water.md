# input
integer array height(length between 1 and 2*10^4; integers between 0 and 10^5)

# output
an integer (the units of rainwater captured)

# steps:
1. right=[] left=[] i=j=k=0 unit=0
2. for i in range(len(height)):
    right.append(maximum of height[0] to height[i] - height[i])
3. for j in range(len(height)):
    left.append(maximum of height[j] to height[len(height)-1] - height[j])
4. for k in range(len(height)):
    unit += min(right[k],left[k])
5. return unit

# requirements
1. write a python function, test it yourself, and put the code into trapping_rain_water.py
2. start with: def trap(self, height: List[int]) -> int: