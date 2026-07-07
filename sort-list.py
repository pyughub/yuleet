from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values: list[int] = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        values.sort()

        if not values:
            return None

        new_head = ListNode(values[0])
        curr = new_head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return new_head

    # merge sort
    def sortList_merge(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        left = self.sortList_merge(head)
        right = self.sortList_merge(right)
        return self._merge(left, right)

    def _merge(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
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
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
    ]

    passed = 0
    for idx, (input_vals, expected) in enumerate(tests, 1):
        head = build_list(input_vals)
        head_merge = build_list(input_vals)
        actual = list_to_values(solution.sortList(head))
        actual_merge = list_to_values(solution.sortList_merge(head_merge))
        ok = actual == expected and actual_merge == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  input={input_vals}  "
            f"array={actual}  merge={actual_merge}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
