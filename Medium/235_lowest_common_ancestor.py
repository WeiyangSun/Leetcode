"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia : "The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant
of itself).”
"""

"""
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2

Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # set starting point at the root of the tree
        current = root

        # iterate until we find the split point or one of the nodes matches
        while current:
            # if both p and q are smaller than current, go to the left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left
            # if both p and q are greater than current, go to the right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # found the split or one node is the ancestor of the other
                return current
