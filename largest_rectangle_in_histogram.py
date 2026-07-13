from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[int] = []
        max_area = 0

        for i in range(len(heights) + 1):
            current = heights[i] if i < len(heights) else 0
            while stack and current < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([2, 2], 4),
        ([1, 1, 1, 1], 4),
        ([5, 4, 3, 2, 1], 9),
        ([1, 2, 3, 4, 5], 9),
    ]

    passed = 0
    for idx, (heights, expected) in enumerate(tests, 1):
        actual = solution.largestRectangleArea(heights)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  heights={heights}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
