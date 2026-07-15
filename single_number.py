from typing import List


def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    tests = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([0, 1, 0], 1),
        ([-1, -1, -2], -2),
        ([7, 3, 7, 3, 9], 9),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        actual = singleNumber(None, nums)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
