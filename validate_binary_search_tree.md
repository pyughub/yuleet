# input
the root node of a binary tree: root

# output
boolean value(signaling if its a BST)

# steps
1. start from the root node: see if all values in left tree<root.val<all values in right tree
2. check the left tree in the same way
3. check the right tree in the same way
4. if all true, return true; else return false

# requirements
1. write a python function, test it yourself, and put the code into validate_binary_search_tree.py
2. start with: # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: