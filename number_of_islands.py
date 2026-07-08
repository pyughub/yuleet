from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def mark_connected(r: int, c: int) -> None:
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or grid[r][c] != "1"
            ):
                return
            grid[r][c] = "2"
            mark_connected(r + 1, c)
            mark_connected(r - 1, c)
            mark_connected(r, c + 1)
            mark_connected(r, c - 1)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    mark_connected(i, j)
                    islands += 1

        return islands


def copy_grid(grid: List[List[str]]) -> List[List[str]]:
    return [row[:] for row in grid]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
        ([], 0),
        ([["0"]], 0),
        ([["1"]], 1),
    ]

    passed = 0
    for idx, (grid, expected) in enumerate(tests, 1):
        actual = solution.numIslands(copy_grid(grid))
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  expected={expected}  actual={actual}  "
            f"grid={grid}"
        )

    print(f"\n{passed}/{len(tests)} passed")
