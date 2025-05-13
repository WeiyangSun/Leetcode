"""
536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.
"""

"""
Example 1:
Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Example 2:
Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]

Example 3:
Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # If string is None
        if not s:
            return None

        def dfs_parser(start_ix: int) -> tuple[Optional[TreeNode], int]:
            scan_ix = start_ix
            if s[start_ix] == '-':
                scan_ix += 1
            while scan_ix < len(s) and s[scan_ix].isdigit():
                scan_ix += 1
            # After identifying the numerical values associate with node i.e. -42 or 42
            node_val = int(s[start_ix:scan_ix])
            node = TreeNode(node_val)

            # Checking for left subtree
            if scan_ix < len(s) and s[scan_ix] == '(':
                node.left, scan_ix = dfs_parser(scan_ix + 1)
                scan_ix += 1

            # Checking for right subtree
            if scan_ix < len(s) and s[scan_ix] == '(':
                node.right, scan_ix = dfs_parser(scan_ix + 1)
                scan_ix += 1

            return node, scan_ix