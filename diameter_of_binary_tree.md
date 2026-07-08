# input
root node of a binary tree: root

# output
an integer

# steps
1. apply DFS to each node and find out the maximum of left tree depth and right tree depth
2. return the sum of the two maximums

# requirements
1. write a python function, test it yourself, and put the code into diameter_of_binary_tree.py
2. start with: # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: