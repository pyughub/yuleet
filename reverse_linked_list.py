from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]

    passed = 0
    for idx, (input_vals, expected) in enumerate(tests, 1):
        head = build_list(input_vals)
        reversed_head = solution.reverseList(head)
        actual = list_to_values(reversed_head)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  input={input_vals}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
