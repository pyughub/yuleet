from typing import List


def findAnagrams(self, s: str, p: str) -> List[int]:
    ana_ind = []
    if len(s) < len(p):
        return ana_ind

    plen = len(p)
    p_sorted = sorted(p)

    for i in range(len(s) - plen + 1):
        if sorted(s[i : i + plen]) == p_sorted:
            ana_ind.append(i)

    return ana_ind


# O(n) time, O(1) space — sliding window + 26-letter count
def findAnagrams_sliding(self, s: str, p: str) -> List[int]:
    if len(s) < len(p):
        return []

    m = len(p)
    need = [0] * 26
    window = [0] * 26
    for ch in p:
        need[ord(ch) - ord("a")] += 1

    ana_ind = []
    for i, ch in enumerate(s):
        window[ord(ch) - ord("a")] += 1
        if i >= m:
            window[ord(s[i - m]) - ord("a")] -= 1
        if i >= m - 1 and window == need:
            ana_ind.append(i - m + 1)

    return ana_ind


if __name__ == "__main__":
    tests = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("aaaaaaa", "aaa", [0, 1, 2, 3, 4]),
        ("a", "a", [0]),
        ("a", "b", []),
    ]

    passed = 0
    for idx, (s, p, expected) in enumerate(tests, 1):
        result = findAnagrams(None, s, p)
        result_sliding = findAnagrams_sliding(None, s, p)
        ok = result == expected and result_sliding == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  sorted={result}  sliding={result_sliding}  "
            f"expected={expected}  s={s!r}  p={p!r}"
        )

    print(f"\n{passed}/{len(tests)} passed")
