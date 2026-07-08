from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root, float("-inf"), float("inf"))

    def isValidBSTInorder(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")

        def inorder(node: Optional[TreeNode]) -> bool:
            nonlocal prev
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= prev:
                return False
            prev = node.val
            return inorder(node.right)

        return inorder(root)


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
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([], True),
        ([1], True),
        ([10, 5, 15, None, None, 6, 20], False),
        ([2, 2, 2], False),
        ([5, 4, 6, None, None, 3, 7], False),
    ]

    methods = [
        ("bounds", solution.isValidBST),
        ("inorder+prev", solution.isValidBSTInorder),
    ]

    for name, method in methods:
        print(f"--- {name} ---")
        passed = 0
        for idx, (tree_vals, expected) in enumerate(tests, 1):
            root = build_tree(tree_vals)
            actual = method(root)
            ok = actual == expected
            passed += ok
            status = "OK" if ok else "FAIL"
            print(
                f"[{idx}] {status}  tree={tree_vals}  "
                f"actual={actual}  expected={expected}"
            )
        print(f"{passed}/{len(tests)} passed\n")
