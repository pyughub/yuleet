from typing import List, Tuple


class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[tuple[str, int]] = []
        cur = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur, num))
                cur = ""
                num = 0
            elif ch == "]":
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += ch

        return cur


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]", "abcabc"),
        ("abc", "abc"),
        ("10[a]", "aaaaaaaaaa"),
        ("a", "a"),
    ]

    passed = 0
    for idx, (s, expected) in enumerate(tests, 1):
        actual = solution.decodeString(s)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  s={s!r}  actual={actual!r}  expected={expected!r}"
        )

    print(f"\n{passed}/{len(tests)} passed")
