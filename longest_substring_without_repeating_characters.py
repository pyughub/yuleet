def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
        return 0

    i = 0
    j = 1
    length = 1
    n = len(s)

    while j < n:
        if len(set(s[i : j + 1])) < j - i + 1:
            i += 1
        else:
            length = max(length, j - i + 1)
            j += 1

    return length


# O(n) time, O(min(n, charset)) space — sliding window + last index map
def lengthOfLongestSubstring_hash(self, s: str) -> int:
    last = {}
    i = 0
    length = 0

    for j, ch in enumerate(s):
        if ch in last and last[ch] >= i:
            i = last[ch] + 1
        last[ch] = j
        length = max(length, j - i + 1)

    return length


if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ]

    passed = 0
    for idx, (s, expected) in enumerate(tests, 1):
        result = lengthOfLongestSubstring(None, s)
        result_hash = lengthOfLongestSubstring_hash(None, s)
        ok = result == expected and result_hash == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  sliding={result}  hash={result_hash}  "
            f"expected={expected}  s={s!r}"
        )

    print(f"\n{passed}/{len(tests)} passed")
