from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    prefix_sums = []
    total = 0
    for num in nums:
        total += num
        prefix_sums.append(total)

    min_prefix = 0
    max_sum = float("-inf")
    for prefix in prefix_sums:
        max_sum = max(max_sum, prefix - min_prefix)
        min_prefix = min(min_prefix, prefix)

    return max_sum


# O(n) time, O(1) space — Kadane's algorithm
def maxSubArray_kadane(self, nums: List[int]) -> int:
    cur = max_sum = nums[0]
    for num in nums[1:]:
        cur = max(num, cur + num)
        max_sum = max(max_sum, cur)
    return max_sum


if __name__ == "__main__":
    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([-2, -1], -1),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        result = maxSubArray(None, nums[:])
        result_kadane = maxSubArray_kadane(None, nums[:])
        ok = result == expected and result_kadane == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  prefix={result}  kadane={result_kadane}  "
            f"expected={expected}  nums={nums}"
        )

    print(f"\n{passed}/{len(tests)} passed")
