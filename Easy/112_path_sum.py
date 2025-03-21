"""
112. Path Sum

Given the root of a binary tree and an integer `targetSum`, return true if the tree has a root-to-leaf path such
that adding up all the values along the path equals `targetSum`.

A leaf is a node with no children.
"""

"""
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: There are one root-to-leaf paths in the tree:
(5 --> 4 --> 11 --> 2): The sum is 22.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false

Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: list[TreeNode], targetSum: int) -> bool:

        # Base Case
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        newSum = targetSum - root.val

        return (self.hasPathSum(root.left, newSum) or self.hasPathSum(root.right, newSum))