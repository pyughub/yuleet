from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_idx[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)


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


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


if __name__ == "__main__":
    solution = Solution()

    tests = [
        (
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            [3, 9, 20, None, None, 15, 7],
        ),
        ([1], [1], [1]),
        ([], [], []),
        ([1, 2], [2, 1], [1, 2]),
    ]

    passed = 0
    for idx, (preorder, inorder, expected) in enumerate(tests, 1):
        root = solution.buildTree(preorder, inorder)
        actual = tree_to_list(root)
        pre_ok = preorder_traversal(root) == preorder
        in_ok = inorder_traversal(root) == inorder
        shape_ok = actual == expected
        ok = shape_ok and pre_ok and in_ok
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  preorder={preorder}  inorder={inorder}  "
            f"actual={actual}  expected={expected}  "
            f"preorder_ok={pre_ok}  inorder_ok={in_ok}"
        )

    print(f"\n{passed}/{len(tests)} passed")
