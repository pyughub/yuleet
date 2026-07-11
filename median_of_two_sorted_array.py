from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = (total + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            a_left = A[i - 1] if i > 0 else float("-inf")
            a_right = A[i] if i < m else float("inf")
            b_left = B[j - 1] if j > 0 else float("-inf")
            b_right = B[j] if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 1:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            if a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1

        raise ValueError("invalid input arrays")


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1], [2, 3, 4, 5, 6], 3.5),
        ([1, 2, 3], [4, 5, 6], 3.5),
        ([1, 2], [1, 2], 1.5),
    ]

    passed = 0
    for idx, (nums1, nums2, expected) in enumerate(tests, 1):
        actual = solution.findMedianSortedArrays(nums1, nums2)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums1={nums1}  nums2={nums2}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
