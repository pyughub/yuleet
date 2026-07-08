from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result: List[List[int]] = []
        queue: list[TreeNode] = [root]

        while queue:
            level: list[int] = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

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
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([], []),
        ([1], [[1]]),
        ([1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]]),
    ]

    passed = 0
    for idx, (tree_vals, expected) in enumerate(tests, 1):
        root = build_tree(tree_vals)
        actual = solution.levelOrder(root)
        ok = actual == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  tree={tree_vals}  "
            f"actual={actual}  expected={expected}"
        )

    print(f"\n{passed}/{len(tests)} passed")
