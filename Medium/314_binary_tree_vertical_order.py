"""
314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
"""

"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns_tracker = defaultdict(list)
        queue = deque([(root, 0)])  # we set root to be in column 0

        left_col_boundary, right_col_boundary = 0, 0

        while queue:
            current_node, col_idx = queue.popleft()
            columns_tracker[col_idx].append(current_node.val)

            left_col_boundary = min(left_col_boundary, col_idx)
            right_col_boundary = max(right_col_boundary, col_idx)

            if current_node.left:
                queue.append((current_node.left, col_idx - 1))
            if current_node.right:
                queue.append((current_node.right, col_idx + 1))

        return [
            columns_tracker[col_idx]
            for col_idx in range(left_col_boundary, right_col_boundary + 1)
        ]
