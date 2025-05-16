"""
1644. Lowest Common Ancestor of a Binary Tree II

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given
nodes, p and q. If either node p or q does not exist in the tree, return null. All values
of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: " The lowest common ancestor of two nodes
p and q in a binary tree T is the lowest node that has both p and q as descendants (where we
allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on 
the path from node x to some leaf node.
"""

"""
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the 
definition of LCA.

Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null

Explanation: Node 10 does not exist in the tree, so return null.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def node_exists(node, target):
            if not node:
                return False
            if node is target:
                return True
            return node_exists(node.left, target) or node_exists(node.right, target)

        # First Scan to check if Node even exists
        if not node_exists(root, p) or not node_exists(root, q):
            return None

        def lca(node):
            # Base Case
            if node is p or node is q:
                return node
            # Second Scan to find LCA if it exists
            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node
            return left or right

        return lca(root)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None

        def dfs(node):
            if not node:
                return (False, False)

            left_p, left_q = dfs(node.left)
            right_p, right_q = dfs(node.right)

            mid_p = node is p
            mid_q = node is q

            found_p = left_p or mid_p or right_p
            found_q = left_q or mid_q or right_q

            if self.ans is None:
                flags = [mid_p, mid_q, left_p or left_q, right_p or right_q]
                if flags.count(True) >= 2:
                    self.ans = node

            return (found_p, found_q)

        found_p, found_q = dfs(root)
        return self.ans if (found_p and found_q) else None
