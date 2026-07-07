from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        i: Optional[ListNode] = dummy
        j: Optional[ListNode] = head

        for _ in range(n - 1):
            if j:
                j = j.next

        while j and j.next:
            i = i.next
            j = j.next

        if i.next:
            i.next = i.next.next

        return dummy.next


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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ]

    passed = 0
    for idx, (values, n, expected) in enumerate(tests, 1):
        head = build_list(values)
        result = solution.removeNthFromEnd(head, n)
        actual = list_to_values(result)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  values={values}  n={n}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
