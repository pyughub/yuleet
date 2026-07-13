from typing import List


class Solution:
    # O(n) time, O(1) space — forward greedy (BFS levels)
    def jump_forward(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break

        return jumps

    # O(n^2) time, O(1) space — backward greedy
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        goal = n - 1

        while goal > 0:
            for i in range(goal):
                if i + nums[i] >= goal:
                    goal = i
                    jumps += 1
                    break

        return jumps


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1], 0),
        ([1, 2], 1),
        ([1, 1, 1, 1], 3),
        ([2, 1, 1, 1, 1], 3),
    ]

    methods = [
        ("jump_forward", solution.jump_forward),
        ("jump", solution.jump),
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
