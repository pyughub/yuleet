from typing import List


def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num
        need = prefix_sum - k
        if need in prefix_map:
            count += prefix_map[need]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count


if __name__ == "__main__":
    tests = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([1], 1, 1),
        ([1], 0, 0),
        ([0, 0, 0], 0, 6),
    ]

    passed = 0
    for idx, (nums, k, expected) in enumerate(tests, 1):
        result = subarraySum(None, nums[:], k)
        ok = result == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(f"[{idx}] {status}  nums={nums}  k={k}  result={result}  expected={expected}")

    print(f"\n{passed}/{len(tests)} passed")
