from typing import List

# O(N * K log K) time, O(N * K) space — sorting key -- my solution
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


# O(N * K) time, O(N * K) space — character count key
def groupAnagrams_count(self, strs: List[str]) -> List[List[str]]:
    groups = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        key = tuple(count)
        groups.setdefault(key, []).append(s)
    return list(groups.values())
