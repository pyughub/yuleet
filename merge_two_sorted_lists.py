from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        counts: dict[int, int] = {}

        for lst in (list1, list2):
            while lst:
                counts[lst.val] = counts.get(lst.val, 0) + 1
                lst = lst.next

        dummy = ListNode()
        curr = dummy
        for val in sorted(counts):
            for _ in range(counts[val]):
                curr.next = ListNode(val)
                curr = curr.next

        return dummy.next

    def mergeTwoLists_two_pointers(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [2], [1, 2]),
        ([1, 1], [1], [1, 1, 1]),
    ]

    passed = 0
    for idx, (list1_vals, list2_vals, expected) in enumerate(tests, 1):
        list1 = build_list(list1_vals)
        list2 = build_list(list2_vals)
        list1_tp = build_list(list1_vals)
        list2_tp = build_list(list2_vals)
        actual = list_to_values(solution.mergeTwoLists(list1, list2))
        actual_tp = list_to_values(
            solution.mergeTwoLists_two_pointers(list1_tp, list2_tp)
        )
        ok = actual == expected and actual_tp == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  list1={list1_vals}  list2={list2_vals}  "
            f"dict={actual}  two_pointers={actual_tp}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
