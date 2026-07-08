# input
an integer array nums arranged in ascending order

# output
a balanced BST made of integers in nums

# steps
1. i=len(nums)//2 
2. make nums[i] the root node; put those to its left on its left tree and right on its right tree
3. for each subtree, do as step2 (recurse)
4. return the BST (check if its balanced)

# requirements
1. write a python function, test it yourself, and put the code into convert_sorted_array_to_binary_search_tree.py
2. start with: # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: