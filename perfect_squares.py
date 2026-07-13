from collections import deque
from functools import lru_cache


class Solution:
    # O(n * sqrt(n)) time, O(n) space — unbounded knapsack + memo
    def numSquares(self, n: int) -> int:
        sq_list = []
        i = 1
        while i * i <= n:
            sq_list.append(i * i)
            i += 1
        sq_list.reverse()

        @lru_cache(maxsize=None)
        def solve(remaining: int) -> int:
            if remaining == 0:
                return 0

            best = remaining
            for sq in sq_list:
                if sq > remaining:
                    continue
                best = min(best, 1 + solve(remaining - sq))

            return best

        return solve(n)

    # O(n * sqrt(n)) time, O(n) space — BFS (shortest path by layers)
    def numSquares_bfs(self, n: int) -> int:
        queue = deque([n])
        seen = {n}
        level = 0

        while queue:
            level += 1
            for _ in range(len(queue)):
                rem = queue.popleft()
                i = 1
                while i * i <= rem:
                    nxt = rem - i * i
                    if nxt == 0:
                        return level
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
                    i += 1


if __name__ == "__main__":
    solution = Solution()

    tests = [
        (12, 3),
        (13, 2),
        (1, 1),
        (4, 1),
        (7, 4),
        (100, 1),
        (15, 4),
    ]

    methods = [
        ("numSquares", solution.numSquares),
        ("numSquares_bfs", solution.numSquares_bfs),
    ]

    for name, method in methods:
        print(f"=== {name} ===")
        passed = 0
        for idx, (n, expected) in enumerate(tests, 1):
            actual = method(n)
            ok = actual == expected
            passed += ok
            status = "OK" if ok else "FAIL"
            print(
                f"[{idx}] {status}  n={n}  "
                f"actual={actual}  expected={expected}"
            )
        print(f"{passed}/{len(tests)} passed\n")
