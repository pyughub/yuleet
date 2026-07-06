from typing import List

# O(n^2) time, O(1) space — two-pointer technique -- my solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# O(n) time, O(n) space — hash map
def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
