from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: list[str] = []
        path: list[str] = []

        def backtrack(open_count: int, unmatched: int) -> None:
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, unmatched + 1)
                path.pop()
            if unmatched > 0:
                path.append(")")
                backtrack(open_count, unmatched - 1)
                path.pop()

        backtrack(0, 0)
        return res


if __name__ == "__main__":
    solution = Solution()

    tests = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ]

    passed = 0
    for idx, (n, expected) in enumerate(tests, 1):
        actual = solution.generateParenthesis(n)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"[{idx}] {status}  n={n}  actual={actual}  expected={expected}")

    print(f"\n{passed}/{len(tests)} passed")
