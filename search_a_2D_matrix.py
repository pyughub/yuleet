from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            if row[0] <= target <= row[-1]:
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True
                    if row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False

        return False


if __name__ == "__main__":
    solution = Solution()

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]

    tests = [
        (matrix, 3, True),
        (matrix, 13, False),
        (matrix, 30, True),
        (matrix, 1, True),
        (matrix, 60, True),
        (matrix, 0, False),
        (matrix, 61, False),
        ([], 1, False),
        ([[1]], 1, True),
        ([[1]], 0, False),
    ]

    passed = 0
    for idx, (grid, target, expected) in enumerate(tests, 1):
        actual = solution.searchMatrix(grid, target)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  target={target}  actual={actual}  "
            f"expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
