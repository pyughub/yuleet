from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if target < min(nums) or target > max(nums):
            return -1

        max_idx = nums.index(max(nums))

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if target >= nums[0]:
            return binary_search(0, max_idx)
        return binary_search(max_idx + 1, len(nums) - 1)

    # O(log n) time, O(1) space — one modified binary search
    def search_one_bs(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([4, 5, 6, 7, 0, 1, 2], 6, 2),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 3], 3, 1),
        ([3, 1], 1, 1),
        ([3, 1], 3, 0),
    ]

    methods = [
        ("search", solution.search),
        ("search_one_bs", solution.search_one_bs),
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
