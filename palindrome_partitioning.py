from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        res: list[list[str]] = []
        path: list[str] = []

        def backtrack(start: int) -> None:
            if start == n:
                res.append(path[:])
                return

            for end in range(start, n):
                if not is_pal[start][end]:
                    continue
                path.append(s[start : end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return res


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("abba", [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]),
        ("", [[]]),
    ]

    passed = 0
    for idx, (s, expected) in enumerate(tests, 1):
        actual = solution.partition(s)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  s={s!r}  actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
