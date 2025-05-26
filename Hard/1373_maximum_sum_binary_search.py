"""
1373. Maximum Sum BST in Binary Tree

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a
binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""

"""
Example 1:
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20

Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:
Input: root = [4,3,null,1,2]
Output: 2

Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:
Input: root = [-4,-2,-5]
Output: 0

Explanation: All values are negatives. Return an empty BST.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def post_order_traversal(node):
            # Base Case: Empty Node is a BST with sum 0, min = inf, max = -inf
            if not node:
                return (True, 0, float("inf"), float("-inf"))  # is_BST, sum = 0, min=inf, max=-inf

            # check left subtree
            left_is_bst, left_sum, left_min, left_max = post_order_traversal(node.left)
            # check right subtree
            right_is_bst, right_sum, right_min, right_max = post_order_traversal(node.right)

            # Check BST property for current subtree
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                # compute sum of BST rooted at node
                curr_sum = left_sum + node.val + right_sum
                # update global maximum sum if necessary
                self.max_sum = max(self.max_sum, curr_sum)
                # return for this subtree
                return (True, curr_sum, min(left_min, node.val), max(right_max, node.val))
            else:
                return (False, 0, 0, 0)

        post_order_traversal(root)
        return self.max_sum
