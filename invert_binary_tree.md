# input
the root node of a binary tree: root

# output
an inverted tree

# steps
1. invert recursively: go down until reaching the leaf nodes and switch the left and right tree nodes; then backtrack until the whole tree is inverted.
2. return root.

# requirements
1. write a python function, test it yourself, and put the code into invert_binary_tree.py
2. start with: # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: