"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of
its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at
level x is maximal.
"""

"""
Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2

Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Edge Case: Empty Tree
        if not root:
            return 0

        queue = deque([root])
        max_sum = float("-inf")
        max_level = 1
        current_level = 0

        while queue:
            current_level += 1
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # update global using level variables
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

        return max_level
