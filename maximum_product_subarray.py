from typing import List


class Solution:
    # O(n) time, O(1) space — track max/min product ending at i
    def maxProduct(self, nums: List[int]) -> int:
        max_ending = min_ending = result = nums[0]

        for num in nums[1:]:
            candidates = (num, max_ending * num, min_ending * num)
            max_ending = max(candidates)
            min_ending = min(candidates)
            result = max(result, max_ending)

        return result


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2], -2),
        ([0, 2], 2),
        ([-2, 3, -4], 24),
        ([2, -5, -2, -4, 3], 24),
        ([-1, -2, -3], 6),
        ([1, 2, 3, 4], 24),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        actual = solution.maxProduct(nums)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
