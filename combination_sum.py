from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(c for c in candidates if c <= target)
        if not candidates:
            return []

        res: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return res


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([1], 2, [[1, 1]]),
    ]

    passed = 0
    for idx, (candidates, target, expected) in enumerate(tests, 1):
        actual = solution.combinationSum(candidates[:], target)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  candidates={candidates}  target={target}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
