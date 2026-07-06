from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_a: list[ListNode] = []
        nodes_b: list[ListNode] = []

        while headA:
            nodes_a.append(headA)
            headA = headA.next
        while headB:
            nodes_b.append(headB)
            headB = headB.next

        i, j = len(nodes_a) - 1, len(nodes_b) - 1
        result: Optional[ListNode] = None

        while i >= 0 and j >= 0 and nodes_a[i].val == nodes_b[j].val:
            if nodes_a[i] is nodes_b[j]:
                result = nodes_a[i]
            i -= 1
            j -= 1

        return result

    def getIntersectionNode_two_pointers(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa is not pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


def build_intersecting_lists(
    list_a: list[int], list_b: list[int], shared: list[int]
) -> tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
    """Build two lists that share a tail starting at `shared[0]`."""
    if not shared:
        head_a = _build_list(list_a)
        head_b = _build_list(list_b)
        return head_a, head_b, None

    shared_nodes = [ListNode(v) for v in shared]
    for idx in range(len(shared_nodes) - 1):
        shared_nodes[idx].next = shared_nodes[idx + 1]

    head_a = _build_list(list_a, shared_nodes[0])
    head_b = _build_list(list_b, shared_nodes[0])
    return head_a, head_b, shared_nodes[0]


def _build_list(values: list[int], tail: Optional[ListNode] = None) -> Optional[ListNode]:
    if not values:
        return tail
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    curr.next = tail
    return head


if __name__ == "__main__":
    solution = Solution()

    tests = [
        {
            "name": "intersect at c1",
            "list_a": [4, 1],
            "list_b": [5, 6, 1],
            "shared": [8, 4, 5],
            "expected_val": 8,
        },
        {
            "name": "intersect at b1",
            "list_a": [1, 9, 1],
            "list_b": [3, 2, 1],
            "shared": [1],
            "expected_val": 1,
        },
        {
            "name": "no intersection",
            "list_a": [2, 6, 4],
            "list_b": [1, 5],
            "shared": [],
            "expected_val": None,
        },
        {
            "name": "both empty",
            "list_a": [],
            "list_b": [],
            "shared": [],
            "expected_val": None,
        },
        {
            "name": "same value different nodes",
            "list_a": [7],
            "list_b": [7],
            "shared": [],
            "expected_val": None,
        },
    ]

    passed = 0
    for idx, test in enumerate(tests, 1):
        head_a, head_b, expected_node = build_intersecting_lists(
            test["list_a"], test["list_b"], test["shared"]
        )
        if test["expected_val"] is None and expected_node is None:
            pass
        elif expected_node is not None:
            assert expected_node.val == test["expected_val"]

        actual = solution.getIntersectionNode(head_a, head_b)
        actual_two = solution.getIntersectionNode_two_pointers(head_a, head_b)
        expected_val = test["expected_val"]
        actual_val = actual.val if actual else None
        actual_two_val = actual_two.val if actual_two else None
        ok = (
            actual is expected_node
            and actual_val == expected_val
            and actual_two is expected_node
            and actual_two_val == expected_val
        )
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  {test['name']}  "
            f"reverse={actual_val}  two_pointers={actual_two_val}  "
            f"expected={expected_val}"
        )

    print(f"\n{passed}/{len(tests)} passed")
