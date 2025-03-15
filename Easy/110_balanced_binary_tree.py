"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
"""

"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: list[TreeNode]) -> bool:

        def check_height(node):
            # Base Case
            if not node:
                return 0

            # Recursively check height of left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            # Recursively check height of right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            # Check height difference at current node
            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return check_height(root) != -1
