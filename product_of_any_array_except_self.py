from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    products = []
    n = len(nums)

    for i in range(n):
        left = 1
        for j in range(i):
            left *= nums[j]

        right = 1
        for j in range(i + 1, n):
            right *= nums[j]

        products.append(left * right)

    return products


# O(n) time, O(1) extra space — prefix + suffix, no division
def productExceptSelf_linear(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([1], [1]),
        ([0, 0], [0, 0]),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        result = productExceptSelf(None, nums[:])
        result_linear = productExceptSelf_linear(None, nums[:])
        ok = result == expected and result_linear == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  brute={result}  linear={result_linear}  "
            f"expected={expected}  nums={nums}"
        )

    print(f"\n{passed}/{len(tests)} passed")
