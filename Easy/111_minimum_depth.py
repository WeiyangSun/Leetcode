"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: list[TreeNode]) -> int:
        if not root:
            return 0

        # Initialize Queue
        queue = deque([(root, 1)]) # (Node, Depth)

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))

        return 0