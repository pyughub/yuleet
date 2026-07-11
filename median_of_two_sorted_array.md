# input
two integer arrays nums1 (m numbers) and nums2 (n numbers) in ascending order

# output
the median of all numbers in the two merged arrays

# steps
1. binary search on the shorter array to choose a partition i so the left half has (m + n + 1) // 2 elements
2. let j = half - i be the partition index in the other array
3. if max(left parts) <= min(right parts), the partition is correct; compute the median from boundary values
4. otherwise move the partition left or right and repeat

# requirements
1. write a python function, test it yourself, and put the code into median_of_two_sorted_array.py
2. start with: def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3. time complexity must be O(log (m + n))
