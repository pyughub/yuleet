from typing import List


class Solution:
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

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        actual = solution.jump(nums)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
