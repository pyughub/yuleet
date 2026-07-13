from typing import List


class Solution:
    # O(n) time, O(1) space — forward greedy with early exit
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)

        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True

        return True

    # O(n) time, O(1) space — backward greedy
    def canJump_backward(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0], True),
        ([0, 1], False),
        ([2, 0, 0], True),
        ([1, 1, 1, 1], True),
    ]

    methods = [
        ("canJump", solution.canJump),
        ("canJump_backward", solution.canJump_backward),
    ]

    for name, method in methods:
        print(f"=== {name} ===")
        passed = 0
        for idx, (nums, expected) in enumerate(tests, 1):
            actual = method(nums)
            ok = actual == expected
            passed += ok
            status = "OK" if ok else "FAIL"
            print(
                f"[{idx}] {status}  nums={nums}  "
                f"actual={actual}  expected={expected}"
            )
        print(f"{passed}/{len(tests)} passed\n")
