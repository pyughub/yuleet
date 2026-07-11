from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        if not word:
            return True

        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        if any(word_count[ch] > board_count[ch] for ch in word_count):
            return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            if board[r][c] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                (r + 1 < rows and dfs(r + 1, c, k + 1))
                or (r - 1 >= 0 and dfs(r - 1, c, k + 1))
                or (c + 1 < cols and dfs(r, c + 1, k + 1))
                or (c - 1 >= 0 and dfs(r, c - 1, k + 1))
            )

            board[r][c] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False


def copy_board(board: List[List[str]]) -> List[List[str]]:
    return [row[:] for row in board]


if __name__ == "__main__":
    solution = Solution()

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    tests = [
        (board, "ABCCED", True),
        (board, "SEE", True),
        (board, "ABCB", False),
        (board, "A", True),
        (board, "Z", False),
        ([], "ABC", False),
        ([["A"]], "", True),
    ]

    passed = 0
    for idx, (grid, word, expected) in enumerate(tests, 1):
        actual = solution.exist(copy_board(grid), word)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  word={word!r}  expected={expected}  "
            f"actual={actual}"
        )

    print(f"\n{passed}/{len(tests)} passed")
