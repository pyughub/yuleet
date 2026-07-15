from typing import List


# O(n^2) time (bubble sort), O(1) space — find ascent, sort suffix, rotate successor to front
def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            k = i
            break

    if k == -1:
        nums.reverse()
        return

    temp = nums[k]

    for i in range(k, n):
        for j in range(k, n - 1 - (i - k)):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    pos = k
    for i in range(k, n):
        if nums[i] == temp:
            pos = i

    successor = nums[pos + 1]
    for i in range(pos + 1, k, -1):
        nums[i] = nums[i - 1]
    nums[k] = successor


# O(n) time, O(1) space — find ascent, swap with next greater, reverse suffix
def nextPermutation_optimized(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            k = i
            break

    if k == -1:
        nums.reverse()
        return

    # suffix nums[k+1:] is descending; find rightmost successor of nums[k]
    for l in range(n - 1, k, -1):
        if nums[l] > nums[k]:
            nums[k], nums[l] = nums[l], nums[k]
            break

    nums[k + 1 :] = reversed(nums[k + 1 :])


if __name__ == "__main__":
    tests = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1], [3, 1, 2]),
        ([1, 5, 1], [5, 1, 1]),
        ([1, 2, 3, 3], [1, 3, 2, 3]),
        ([2, 1, 3, 3], [2, 3, 1, 3]),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([2, 1], [1, 2]),
    ]

    for name, fn in (
        ("nextPermutation", nextPermutation),
        ("nextPermutation_optimized", nextPermutation_optimized),
    ):
        passed = 0
        print(f"=== {name} ===")
        for idx, (nums, expected) in enumerate(tests, 1):
            arr = nums[:]
            fn(None, arr)
            ok = arr == expected
            passed += ok
            status = "OK" if ok else "FAIL"
            print(
                f"[{idx}] {status}  nums={nums}  "
                f"actual={arr}  expected={expected}"
            )
        print(f"{passed}/{len(tests)} passed\n")
