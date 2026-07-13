from collections import defaultdict, deque
from typing import List


class Solution:
    # O(n^2 * m) time, O(n) space — DFS + memo (m = len(wordDict))
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo: dict[int, bool] = {}

        def can_break(start: int) -> bool:
            if start == n:
                return True
            if start in memo:
                return memo[start]

            first_char = s[start]
            for word in wordDict:
                if not word.startswith(first_char):
                    continue
                end = start + len(word)
                if end > n or s[start:end] != word:
                    continue
                if can_break(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return can_break(0)

    # O(n^2 * L) time, O(n) space — bottom-up DP + set
    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

    # O(n * max_len * L) time, O(n) space — DP + set + max_len bound
    def wordBreak_dp_maxlen(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return len(s) == 0

        word_set = set(wordDict)
        n = len(s)
        max_len = max(len(word) for word in wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for length in range(1, min(max_len, n - i) + 1):
                if s[i : i + length] in word_set:
                    dp[i + length] = True

        return dp[n]

    # O(n^2 * L) time, O(n + m) space — DFS + memo, index by first char
    def wordBreak_by_first(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        by_first: dict[str, list[str]] = defaultdict(list)
        for word in wordDict:
            by_first[word[0]].append(word)

        memo: dict[int, bool] = {}

        def can_break(start: int) -> bool:
            if start == n:
                return True
            if start in memo:
                return memo[start]

            for word in by_first[s[start]]:
                end = start + len(word)
                if end > n or s[start:end] != word:
                    continue
                if can_break(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return can_break(0)

    # O(n^2 * L) time, O(n) space — BFS over start positions
    def wordBreak_bfs(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        queue = deque([0])
        seen = {0}

        while queue:
            start = queue.popleft()
            for end in range(start + 1, n + 1):
                if s[start:end] not in word_set:
                    continue
                if end == n:
                    return True
                if end not in seen:
                    seen.add(end)
                    queue.append(end)

        return False


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("a", ["a"], True),
        ("a", ["b"], False),
        ("bb", ["a", "b", "bbb", "bbbb"], True),
        ("bb", ["a", "bbb", "bbbb"], False),
        ("cars", ["car", "ca", "rs"], True),
    ]

    methods = [
        ("wordBreak", solution.wordBreak),
        ("wordBreak_dp", solution.wordBreak_dp),
        ("wordBreak_dp_maxlen", solution.wordBreak_dp_maxlen),
        ("wordBreak_by_first", solution.wordBreak_by_first),
        ("wordBreak_bfs", solution.wordBreak_bfs),
    ]

    for name, method in methods:
        print(f"=== {name} ===")
        passed = 0
        for idx, (s, word_dict, expected) in enumerate(tests, 1):
            actual = method(s, word_dict)
            ok = actual == expected
            passed += ok
            status = "OK" if ok else "FAIL"
            print(
                f"[{idx}] {status}  s={s!r}  wordDict={word_dict}  "
                f"actual={actual}  expected={expected}"
            )
        print(f"{passed}/{len(tests)} passed\n")
