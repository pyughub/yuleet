from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        original_vals: list[int] = []
        curr = head
        while curr:
            original_vals.append(curr.val)
            curr = curr.next

        prev: Optional[ListNode] = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr = prev
        for val in original_vals:
            if not curr or curr.val != val:
                return False
            curr = curr.next

        return True

    def isPalindrome_half_reverse(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev: Optional[ListNode] = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


def build_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3], False),
    ]

    passed = 0
    for idx, (input_vals, expected) in enumerate(tests, 1):
        head = build_list(input_vals)
        head_half = build_list(input_vals)
        actual = solution.isPalindrome(head)
        actual_half = solution.isPalindrome_half_reverse(head_half)
        ok = actual == expected and actual_half == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  input={input_vals}  "
            f"reverse={actual}  half_reverse={actual_half}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
