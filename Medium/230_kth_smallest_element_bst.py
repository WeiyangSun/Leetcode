"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the k-th smallest value (1-indexed)
of all the values of the nodes in the tree.
"""

"""
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0 # initialize counter for visited nodes
        self.result = None # initialize result to store the k-th smallest value

        def inOrderTraversal(node):
            # Base Case
            if not node:
                return

            inOrderTraversal(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            if self.result is not None:
                return
            inOrderTraversal(node.right)

        inOrderTraversal
        return self.result