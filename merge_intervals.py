from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged


if __name__ == "__main__":
    tests = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([], []),
    ]

    passed = 0
    for idx, (intervals, expected) in enumerate(tests, 1):
        result = merge(None, [iv[:] for iv in intervals])
        ok = result == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"[{idx}] {status}  result={result}  expected={expected}")

    print(f"\n{passed}/{len(tests)} passed")
