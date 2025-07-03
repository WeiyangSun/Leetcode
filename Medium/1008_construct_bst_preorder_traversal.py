"""
1008. Construct Binary Search Tree from Preorder Traversal

Given an array of integers preorder, which represents the preorder traversal
of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree
with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of
Node.left has a value strictly less than Node.val, and any descendant of Node.right
has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then
traverses Node.left, then traverses Node.right.
"""

"""
Example 1:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Example 2:
Input: preorder = [1,3]
Output: [1,null,3]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def build(bound=float("inf")):
            # if no elements left or current value exceeds bound, return None
            if self.i == len(preorder) or preorder[self.i] > bound:
                return None

            root_val = preorder[self.i]  # take current value as root
            self.i += 1
            root = TreeNode(root_val)

            root.left = build(root_val)
            root.right = build(bound)  # values > root_val and < bound
            return root

        self.i = 0
        return build()


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        idx = 0  # used to keep track of current index in preorder list

        def helper(lower, upper):
            nonlocal idx
            # if all nodes are processed, return None
            if idx == len(preorder):
                return None

            val = preorder[idx]
            # if val is outside of bounds, then it doesn't belong in this subtree
            if val < lower or val > upper:
                return None

            idx += 1
            # This utilizes preorder traversal
            root = TreeNode(val)
            # using the lower and upper bounds utilizes BST properties
            root.left = helper(lower, val - 1)  # left subtree must be < val
            root.right = helper(val + 1, upper)  # right subtree must be > val

            return root

        return helper(float("-inf"), float("inf"))