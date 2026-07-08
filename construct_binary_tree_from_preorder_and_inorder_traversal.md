# input
two integer arrays preorder and inorder

# output
a binary tree constructed from the two arrays

# steps
1. the first element of preorder is root
2. find this element in inorder and those to its left are the values of the left tree; it is the same with right
3. (if preorder has more than two elements)the second element of preorder is the root node of left subtree; construct the left subtree in the same way as step2; the third element of preorder is the root node of right subtree--the rest is the same.
4. return the constructed tree(root node).

# requirements
1. write a python function, test it yourself, and put the code into construct_binary_tree_from_preorder_and_inorder_traversal.py
2. start with: # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: