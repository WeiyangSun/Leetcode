"""
1110. Delete Nodes and Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union
of trees).

Return the roots of the trees in the remaining forest. You may return the result in any
order.
"""

"""
Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete) #removes duplicates
        remaining_forest = []

        def dfs(node, is_root):
            if not node:
                return None

            node.left = dfs(node.left, node.val in delete_set)
            node.right = dfs(node.right, node.val in delete_set)

            if node.val in delete_set:
                return None

            if is_root:
                remaining_forest.append(node)
            return node

        dfs(root, True)
        return remaining_forest