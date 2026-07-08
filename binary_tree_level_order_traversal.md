# input
the root node of a binary tree: root

# output
level order traversal (layer by layer, left to right)

# steps
1. use BFS with a queue: enqueue the root, then process nodes level by level; for each level, collect all node values left to right, then enqueue their children for the next level.
2. return the result.

# requirements
1. write a python function, test it yourself, and put the code into binary_tree_level_order_traversal.py
2. start with: def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
