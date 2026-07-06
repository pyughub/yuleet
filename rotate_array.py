from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n
    original = nums[:]
    for i in range(n):
        nums[(k + i) % n] = original[i]


def _reverse(nums: List[int], left: int, right: int) -> None:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# O(n) time, O(1) space — reverse whole array, then reverse two parts
def rotate_reverse(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n
    _reverse(nums, 0, n - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, n - 1)


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2], 1, [2, 1]),
        ([1], 0, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]

    passed = 0
    for idx, (nums, k, expected) in enumerate(tests, 1):
        arr = nums[:]
        rotate(None, arr, k)
        arr_rev = nums[:]
        rotate_reverse(None, arr_rev, k)
        ok = arr == expected and arr_rev == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  k={k}  copy={arr}  reverse={arr_rev}  "
            f"expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
