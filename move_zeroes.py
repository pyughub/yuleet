from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nonzero = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[nonzero] = nums[j]
            nonzero += 1
    for i in range(nonzero, len(nums)):
        nums[i] = 0


# O(n) time, O(1) space — single pass, swap non-zero forward
def moveZeroes_swap(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nonzero = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[nonzero], nums[j] = nums[j], nums[nonzero]
            nonzero += 1
