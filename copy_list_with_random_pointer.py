from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        old_to_new: dict[Node, Node] = {}
        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]

    def copyRandomList_interleave(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            next_orig = copy.next
            curr.next = next_orig
            copy.next = next_orig.next if next_orig else None
            curr = next_orig

        return copy_head


def build_random_list(pairs: list[list]) -> Optional[Node]:
    """Build a list from [[val, random_index], ...]; random_index can be None."""
    if not pairs:
        return None

    nodes = [Node(pair[0]) for pair in pairs]
    for idx in range(len(nodes) - 1):
        nodes[idx].next = nodes[idx + 1]

    for idx, pair in enumerate(pairs):
        random_index = pair[1]
        if random_index is not None:
            nodes[idx].random = nodes[random_index]

    return nodes[0]


def list_to_pairs(head: Optional[Node]) -> list[list]:
    nodes: list[Node] = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    index_of = {node: idx for idx, node in enumerate(nodes)}
    pairs: list[list] = []
    for node in nodes:
        random_index = index_of[node.random] if node.random else None
        pairs.append([node.val, random_index])
    return pairs


def uses_only_copy_nodes(original: Optional[Node], copied: Optional[Node]) -> bool:
    original_nodes = set()
    curr = original
    while curr:
        original_nodes.add(curr)
        curr = curr.next

    curr = copied
    while curr:
        if curr in original_nodes:
            return False
        if curr.random and curr.random in original_nodes:
            return False
        curr = curr.next

    return True


if __name__ == "__main__":
    solution = Solution()

    tests = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
        [],
    ]

    passed = 0
    for idx, input_pairs in enumerate(tests, 1):
        head = build_random_list(input_pairs)
        head_interleave = build_random_list(input_pairs)
        copied = solution.copyRandomList(head)
        copied_interleave = solution.copyRandomList_interleave(head_interleave)
        actual_pairs = list_to_pairs(copied)
        actual_interleave = list_to_pairs(copied_interleave)
        ok = (
            actual_pairs == input_pairs
            and actual_interleave == input_pairs
            and uses_only_copy_nodes(head, copied)
            and uses_only_copy_nodes(head_interleave, copied_interleave)
        )
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  input={input_pairs}  "
            f"dict={actual_pairs}  interleave={actual_interleave}  "
            f"expected={input_pairs}"
        )

    print(f"\n{passed}/{len(tests)} passed")
