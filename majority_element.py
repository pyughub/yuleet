from typing import List


# O(n) time, O(1) space — Boyer-Moore voting: majority survives all cancellations
def majorityElement(self, nums: List[int]) -> int:
    candidate = nums[0]
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


if __name__ == "__main__":
    tests = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 1, 2, 2], 1),
        ([-1, -1, 2], -1),
        ([6, 5, 5], 5),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        actual = majorityElement(None, nums)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
