from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    chains = {}

    for num in nums:
        if any(start <= num < end for start, end in chains.items()):
            continue

        head = None
        for start, end in chains.items():
            if num == end:
                chains[start] += 1
                head = start
                break

        if head is None:
            chains[num] = num + 1
            head = num
            tail = num + 1
            if tail in chains and head != tail:
                chains[head] = chains[tail]
                del chains[tail]
        else:
            tail = chains[head]
            if tail in chains and head != tail:
                chains[head] = chains[tail]
                del chains[tail]

    if not chains:
        return 0
    return max(end - start for start, end in chains.items())


# O(n) time, O(n) space — hash set, only count from sequence starts
def longestConsecutive_set(self, nums: List[int]) -> int:
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num - 1 in num_set:
            continue
        current = num
        length = 1
        while current + 1 in num_set:
            current += 1
            length += 1
        max_len = max(max_len, length)

    return max_len
