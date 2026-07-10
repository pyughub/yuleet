from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        path: list[int] = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res


def sorted_permutations(nums: list[int]) -> list[list[int]]:
    return sorted(Solution().permute(nums))


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        actual = sorted_permutations(nums)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"[{idx}] {status}  nums={nums}  actual={actual}  expected={expected}")

    print(f"\n{passed}/{len(tests)} passed")
