from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []

        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        return result


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


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, None, 2, 3], [1, 3, 2]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
    ]

    passed = 0
    for idx, (tree_vals, expected) in enumerate(tests, 1):
        root = build_tree(tree_vals)
        actual = solution.inorderTraversal(root)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  tree={tree_vals}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
