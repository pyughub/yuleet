from typing import List


class Solution:
    # O(n^2) time, O(n) space — DP: dp[i] = LIS length ending at i
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        ([4, 10, 4, 3, 8, 9], 3),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        actual = solution.lengthOfLIS(nums)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
