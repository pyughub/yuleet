from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        i = len(nums) // 2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i + 1 :])
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


def collect_values(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    return collect_values(root.left) + [root.val] + collect_values(root.right)


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(
            node.right, node.val, high
        )

    return validate(root, float("-inf"), float("inf"))


def is_balanced(root: Optional[TreeNode]) -> bool:
    def check(node: Optional[TreeNode]) -> tuple[bool, int]:
        if not node:
            return True, 0
        left_ok, left_h = check(node.left)
        right_ok, right_h = check(node.right)
        balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
        return balanced, 1 + max(left_h, right_h)

    return check(root)[0]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]),
        ([], []),
        ([0], [0]),
        ([1, 3], [3, 1]),
        ([1, 2, 3, 4, 5, 6, 7], [4, 2, 6, 1, 3, 5, 7]),
    ]

    passed = 0
    for idx, (nums, expected) in enumerate(tests, 1):
        root = solution.sortedArrayToBST(nums)
        actual = tree_to_list(root)
        shape_ok = actual == expected
        values_ok = collect_values(root) == nums
        bst_ok = is_valid_bst(root)
        balanced_ok = is_balanced(root) if nums else True
        ok = shape_ok and values_ok and bst_ok and balanced_ok
        passed += ok
        status = "OK" if ok else "FAIL"
        print(
            f"[{idx}] {status}  nums={nums}  "
            f"actual={actual}  expected={expected}  "
            f"bst={bst_ok}  balanced={balanced_ok}"
        )

    print(f"\n{passed}/{len(tests)} passed")
