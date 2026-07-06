from typing import List


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result: List[int] = []
    i = j = 0
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        i, j = top, left

        while j <= right:
            result.append(matrix[i][j])
            j += 1
        top += 1

        i, j = top, right
        while i <= bottom:
            result.append(matrix[i][j])
            i += 1
        right -= 1

        if top <= bottom:
            i, j = bottom, right
            while j >= left:
                result.append(matrix[i][j])
                j -= 1
            bottom -= 1

        if left <= right:
            i, j = bottom, left
            while i >= top:
                result.append(matrix[i][j])
                i -= 1
            left += 1

    return result


if __name__ == "__main__":
    tests = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[1]], [1]),
        ([[1, 2]], [1, 2]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([], []),
    ]

    passed = 0
    for idx, (matrix, expected) in enumerate(tests, 1):
        actual = spiralOrder(None, matrix)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"[{idx}] {status}  actual={actual}  expected={expected}")

    print(f"\n{passed}/{len(tests)} passed")
