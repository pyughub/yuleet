class Solution:
    # O(n^2) time, O(n^2) space — DP: dp[i][j] = whether s[i..j] is palindrome
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length

        return s[start : start + max_len]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("ac", {"a", "c"}),
        ("aaaa", {"aaaa"}),
        ("abb", {"bb"}),
        ("ccc", {"ccc"}),
        ("racecar", {"racecar"}),
    ]

    passed = 0
    for idx, (s, expected_set) in enumerate(tests, 1):
        actual = solution.longestPalindrome(s)
        ok = actual in expected_set
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  s={s!r}  "
            f"actual={actual!r}  expected_one_of={expected_set}"
        )

    print(f"\n{passed}/{len(tests)} passed")
