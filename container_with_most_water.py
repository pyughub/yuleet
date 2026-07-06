from typing import List


def maxArea(self, height: List[int]) -> int:
    maxarea = 0
    i = 0
    j = len(height) - 1
    while j > i:
        area = (j - i) * min(height[i], height[j])
        if area > maxarea:
            maxarea = area
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return maxarea
