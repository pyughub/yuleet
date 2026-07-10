from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: list[list[int]] = []

        for size in range(len(nums) + 1):
            path: list[int] = []

            def backtrack(start: int) -> None:
                if len(path) == size:
                    res.append(path[:])
                    return
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    path.append(nums[i])
                    backtrack(i + 1)
                    path.pop()

            backtrack(0)

        return res

    def subsets_single_pass(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int) -> None:
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


def sorted_subsets(subsets: list[list[int]]) -> list[list[int]]:
    return sorted(subsets, key=lambda s: (len(s), s))


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([0, 1], [[], [0], [1], [0, 1]]),
        ([1], [[], [1]]),
        ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ]

    single_pass_order = [
        ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
    ]

    passed = 0
    total = 0

    print("subsets (by size):")
    for idx, (nums, expected) in enumerate(tests, 1):
        total += 1
        actual = solution.subsets(nums[:])
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"  [{idx}] {status}  nums={nums}")

    print("\nsubsets_single_pass (DFS order):")
    for idx, (nums, expected) in enumerate(single_pass_order, 1):
        total += 1
        actual = solution.subsets_single_pass(nums[:])
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"  [{idx}] {status}  nums={nums}  actual={actual}")

    print("\nsingle_pass matches by-size content:")
    for idx, (nums, expected) in enumerate(tests, 1):
        total += 1
        by_size = sorted_subsets(solution.subsets(nums[:]))
        single = sorted_subsets(solution.subsets_single_pass(nums[:]))
        ok = single == by_size == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"  [{idx}] {status}  nums={nums}")

    print(f"\n{passed}/{total} passed")
