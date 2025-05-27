"""
968. Binary Tree Cameras

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can
monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
"""

"""
Example 1:
Input: root = [0,0,null,0,0]
Output: 1

Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2

Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera_count = 0

        # returns:
        # 0 - This node needs to be covered
        # 1 - Camera is placed at this node
        # 2 - This node is covered by its child
        def dfs(node):
            # Base Case - Null Nodes are considered covered
            if not node:
                return 2

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.camera_count += 1
                return 1

            if left == 1 or right == 1:
                return 2

            return 0

        if dfs(root) == 0:
            self.camera_count += 1

        return self.camera_count
