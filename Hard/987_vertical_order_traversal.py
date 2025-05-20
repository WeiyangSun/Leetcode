"""
987. Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1)
and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column
index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes
in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
"""

"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]

Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
            1 is at the top, so it comes first.
            5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]

Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_tracker = defaultdict(list)
        left_col_boundary, right_col_boundary = 0, 0
        queue = deque([(root, 0, 0)])  # node, col, row

        while queue:
            curr_node, curr_col, curr_row = queue.popleft()
            column_tracker[curr_col].append((curr_row, curr_node.val))

            left_col_boundary = min(left_col_boundary, curr_col)
            right_col_boundary = max(right_col_boundary, curr_col)

            if curr_node.left:
                queue.append((curr_node.left, curr_col - 1, curr_row + 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_col + 1, curr_row + 1))

        output = []
        for col_idx in range(left_col_boundary, right_col_boundary + 1):
            output.append([val for _, val in sorted(column_tracker[col_idx])])

        return output


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0, 0)])  # (node, col, row)
        coordinates = []

        while queue:
            curr_node, curr_col, curr_row = queue.popleft()
            coordinates.append((curr_col, curr_row, curr_node.val))

            if curr_node.left:
                queue.append((curr_node.left, curr_col - 1, curr_row + 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_col + 1, curr_row + 1))

        coordinates.sort()  # sort by column, row then value
        cols = defaultdict(list)
        for col, row, val in coordinates:
            cols[col].append(
                val
            )  # now values in within rows are in correct order but col is out of order
        return [cols[x] for x in sorted(cols)]  # this sort is to make the cols in order
