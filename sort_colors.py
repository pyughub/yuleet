from typing import List


# O(n) time, O(1) space — Dutch national flag: 3-way partition with lo/mid/hi
def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    lo = mid = 0
    hi = len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1


if __name__ == "__main__":
    tests = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([1, 0, 1, 0, 2, 1], [0, 0, 1, 1, 1, 2]),
        ([2, 1, 0], [0, 1, 2]),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        arr = nums[:]
        sortColors(None, arr)
        ok = arr == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={arr}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
