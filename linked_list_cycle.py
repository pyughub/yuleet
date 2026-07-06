from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited: set[ListNode] = set()
        curr = head

        while curr:
            visited.add(curr)
            if curr.next and curr.next in visited:
                return True
            curr = curr.next

        return False

    def hasCycle_floyd(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def build_cyclic_list(values: list[int], pos: int) -> Optional[ListNode]:
    """Build a list; if pos >= 0, tail connects to the node at index pos."""
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for idx in range(len(nodes) - 1):
        nodes[idx].next = nodes[idx + 1]

    if pos >= 0:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        {"values": [3, 2, 0, -4], "pos": 1, "expected": True},
        {"values": [1, 2], "pos": 0, "expected": True},
        {"values": [1], "pos": -1, "expected": False},
        {"values": [], "pos": -1, "expected": False},
        {"values": [1, 2, 3, 4, 5], "pos": -1, "expected": False},
        {"values": [1], "pos": 0, "expected": True},
    ]

    passed = 0
    for idx, test in enumerate(tests, 1):
        head = build_cyclic_list(test["values"], test["pos"])
        head_floyd = build_cyclic_list(test["values"], test["pos"])
        actual = solution.hasCycle(head)
        actual_floyd = solution.hasCycle_floyd(head_floyd)
        expected = test["expected"]
        ok = actual == expected and actual_floyd == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  values={test['values']}  pos={test['pos']}  "
            f"visited={actual}  floyd={actual_floyd}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
