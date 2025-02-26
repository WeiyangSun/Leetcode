"""
99. Recover Binary Search Tree

You are given the root of a binary search tree, where the values of exactly two nodes of the tree were
swapped by mistake. Recover the tree without changing its structure.
"""

"""
Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]

Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]

Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: [TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Keeping track of nodes during traversal
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            # Searching Left Sub-treees
            inorder(node.left)

            # if prev node is set and current node value is < prev node - out of order
            if self.prev and node.val < self.prev.val:
                # First time happening - mark first node
                if not self.first:
                    self.first = self.prev
                # update second node to current node when there is a violation
                self.second = node

            self.prev = node  # move node forward

            # Search Right Sub-trees
            inorder(node.right)

        # Finding two swapped nodes
        inorder(root)

        # Perform swap
        self.first.val, self.second.val = self.second.val, self.first.val
