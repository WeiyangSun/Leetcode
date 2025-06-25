"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
"""

"""
Example 1:
Input: root = [1,2,3,4,5]
Output: 3

Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            # Base Case: if node is None, height is 0
            if not node:
                return 0

            # Recurse down Left Side
            left_height = dfs(node.left)
            # Recurse down Right Side
            right_height = dfs(node.right)
            # Update max diameter if path through this node is larger
            max_diameter = max(max_diameter, left_height + right_height)
            # Height of this node is 1 + max of left or right substree height
            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diameter
