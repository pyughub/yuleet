from typing import List


def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    rows = [False] * m
    cols = [False] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0


# O(m*n) time, O(1) extra space — use first row/col as markers
def setZeroes_constant(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0


if __name__ == "__main__":
    tests = [
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        ),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
        ([[1]], [[1]]),
        ([[0]], [[0]]),
        ([[1, 0]], [[0, 0]]),
    ]

    passed = 0
    for idx, (matrix, expected) in enumerate(tests, 1):
        arr = [row[:] for row in matrix]
        arr_const = [row[:] for row in matrix]
        setZeroes(None, arr)
        setZeroes_constant(None, arr_const)
        ok = arr == expected and arr_const == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  markers={arr}  constant={arr_const}  "
            f"expected={expected}  matrix={matrix}"
        )

    print(f"\n{passed}/{len(tests)} passed")
