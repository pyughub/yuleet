from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        found = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found = mid
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if found == -1:
            return [-1, -1]

        start = found
        end = found
        while start - 1 >= 0 and nums[start - 1] == target:
            start -= 1
        while end + 1 < len(nums) and nums[end + 1] == target:
            end += 1

        return [start, end]

    # O(log n) time, O(1) space — two binary searches
    def searchRange_two_bs(self, nums: List[int], target: int) -> List[int]:
        def find_bound(find_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if find_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        start = find_bound(True)
        if start == -1:
            return [-1, -1]
        return [start, find_bound(False)]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2], 2, [0, 1]),
        ([2, 2], 1, [-1, -1]),
        ([1, 2, 2, 2, 3], 2, [1, 3]),
    ]

    methods = [
        ("searchRange", solution.searchRange),
        ("searchRange_two_bs", solution.searchRange_two_bs),
    ]

    for name, method in methods:
        print(f"=== {name} ===")
        passed = 0
        for idx, (nums, target, expected) in enumerate(tests, 1):
            actual = method(nums, target)
            ok = actual == expected
            passed += ok
            status = "OK" if ok else "FAIL"
            print(
                f"[{idx}] {status}  nums={nums}  target={target}  "
                f"actual={actual}  expected={expected}"
            )
        print(f"{passed}/{len(tests)} passed\n")
