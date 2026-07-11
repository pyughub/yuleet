from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack: list[int] = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)

        return answer


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([55], [0]),
        ([100, 80], [0, 0]),
        ([34, 80, 80, 34, 34, 80, 80, 80, 80], [1, 0, 0, 2, 1, 0, 0, 0, 0]),
    ]

    passed = 0
    for idx, (temperatures, expected) in enumerate(tests, 1):
        actual = solution.dailyTemperatures(temperatures)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  temperatures={temperatures}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
