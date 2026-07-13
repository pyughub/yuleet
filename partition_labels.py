from typing import List


class Solution:
    # O(n) time, O(1) space — last index + greedy scan
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}

        result: List[int] = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
        ("ababcc", [4, 2]),
        ("a", [1]),
        ("aa", [2]),
        ("caedbdedda", [1, 9]),
    ]

    passed = 0
    for idx, (s, expected) in enumerate(tests, 1):
        actual = solution.partitionLabels(s)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  s={s!r}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
