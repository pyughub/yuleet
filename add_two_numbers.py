from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        total = 0
        dec = 1

        while l1 and l2:
            total += (l1.val + l2.val) * dec
            dec *= 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            total += l1.val * dec
            dec *= 10
            l1 = l1.next

        while l2:
            total += l2.val * dec
            dec *= 10
            l2 = l2.next

        if total == 0:
            return ListNode(0)

        dummy = ListNode()
        curr = dummy
        while total > 0:
            curr.next = ListNode(total % 10)
            total //= 10
            curr = curr.next

        return dummy.next

    def addTwoNumbers_carry(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, digit = divmod(val, 10)
            curr.next = ListNode(digit)
            curr = curr.next

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
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([5], [5], [0, 1]),
        ([1], [9, 9], [0, 0, 1]),
    ]

    passed = 0
    for idx, (l1_vals, l2_vals, expected) in enumerate(tests, 1):
        l1 = build_list(l1_vals)
        l2 = build_list(l2_vals)
        l1_carry = build_list(l1_vals)
        l2_carry = build_list(l2_vals)
        actual = list_to_values(solution.addTwoNumbers(l1, l2))
        actual_carry = list_to_values(solution.addTwoNumbers_carry(l1_carry, l2_carry))
        ok = actual == expected and actual_carry == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  l1={l1_vals}  l2={l2_vals}  "
            f"int={actual}  carry={actual_carry}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
