from typing import List


class Solution:
    # O(n) time, O(n) space — backward DP
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([0], 0),
        ([1], 1),
        ([2, 1], 2),
        ([1, 2], 2),
        ([5, 1, 2, 5], 10),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        actual = solution.rob(nums)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
