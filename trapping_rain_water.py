from typing import List


def trap(self, height: List[int]) -> int:
    n = len(height)
    right = []
    left = []
    unit = 0

    max_from_left = 0
    for i in range(n):
        max_from_left = max(max_from_left, height[i])
        right.append(max_from_left - height[i])

    max_from_right = 0
    for j in range(n - 1, -1, -1):
        max_from_right = max(max_from_right, height[j])
        left.append(max_from_right - height[j])
    left.reverse()

    for k in range(n):
        unit += min(right[k], left[k])

    return unit


# O(n) time, O(1) space — two pointers
def trap_two_pointer(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    unit = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                unit += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                unit += right_max - height[right]
            right -= 1

    return unit


if __name__ == "__main__":
    tests = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([5, 5, 1, 7, 1, 1, 5, 2, 7, 6], 23),
        ([4, 2, 0, 3, 2, 5], 9),
        ([4, 2, 3], 1),
        ([5], 0),
        ([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3], 83),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 0),
        ([3, 0, 0, 2, 0, 4], 10),
        ([2, 0, 2], 2),
    ]

    passed = 0
    for idx, (height, expected) in enumerate(tests, 1):
        nums = height[:]
        result = trap(None, nums)
        result_tp = trap_two_pointer(None, height)
        ok = result == expected and result_tp == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  trap={result}  two_pointer={result_tp}  "
            f"expected={expected}  height={height}"
        )

    print(f"\n{passed}/{len(tests)} passed")
