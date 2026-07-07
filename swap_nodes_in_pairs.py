from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        prev_pair_tail: Optional[ListNode] = None

        while head and head.next:
            temp = head.next.next
            second = head.next
            head.next.next = head
            head.next = temp

            if prev_pair_tail:
                prev_pair_tail.next = second

            prev_pair_tail = head
            head = temp

        return new_head


def build_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def list_to_values(head: Optional[ListNode]) -> list[int]:
    values: list[int] = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2], [2, 1]),
    ]

    passed = 0
    for idx, (input_vals, expected) in enumerate(tests, 1):
        head = build_list(input_vals)
        result = solution.swapPairs(head)
        actual = list_to_values(result)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  input={input_vals}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
