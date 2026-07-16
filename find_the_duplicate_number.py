from typing import List


# O(n) time, O(1) space — Floyd cycle detection; nums[i] as next pointer
def findDuplicate(self, nums: List[int]) -> int:
    i = j = 0
    while True:
        i = nums[i]
        j = nums[nums[j]]
        if i == j:
            break

    i = 0
    while i != j:
        i = nums[i]
        j = nums[j]
    return i


# O(n) time, O(n) space — set tracks seen values; first repeat is the duplicate
def findDuplicate_set(self, nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


if __name__ == "__main__":
    tests = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
        ([2, 2, 2, 2, 2], 2),
        ([1, 4, 6, 6, 6, 2, 3], 6),
        ([4, 3, 1, 4, 2], 4),
    ]

    for name, fn in (
        ("findDuplicate", findDuplicate),
        ("findDuplicate_set", findDuplicate_set),
    ):
        passed = 0
        print(f"=== {name} ===")
        for idx, (nums, expected) in enumerate(tests, 1):
            original = nums[:]
            actual = fn(None, nums)
            unchanged = nums == original
            ok = actual == expected and unchanged
            passed += ok
            status = "OK" if ok else "FAIL"
            print(
                f"[{idx}] {status}  nums={original}  "
                f"actual={actual}  expected={expected}  "
                f"unchanged={unchanged}"
            )
        print(f"{passed}/{len(tests)} passed\n")
