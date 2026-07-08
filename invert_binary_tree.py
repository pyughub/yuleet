from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: list[TreeNode] = [root]
    idx = 1

    while queue and idx < len(values):
        node = queue.pop(0)
        if idx < len(values) and values[idx] is not None:
            node.left = TreeNode(values[idx])
            queue.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            queue.append(node.right)
        idx += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root:
        return []

    result: list[Optional[int]] = []
    queue: list[Optional[TreeNode]] = [root]

    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
    ]

    passed = 0
    for idx, (tree_vals, expected) in enumerate(tests, 1):
        root = build_tree(tree_vals)
        inverted = solution.invertTree(root)
        actual = tree_to_list(inverted)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  tree={tree_vals}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
