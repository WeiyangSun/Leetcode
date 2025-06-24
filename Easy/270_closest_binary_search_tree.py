"""
270. Closest Binary Search Tree Value

Given the root of a binary search tree and a target value, return the
value in the BST that is closest to the target. If there are multiple
answers, print the smallest.
"""

"""
Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # initialize closest to root val first
        closest = root.val
        current_node = root  # set current pointer to root

        while current_node:
            # if the current val is closer to target, update closest
            if (abs(current_node.val - target) < abs(closest - target)) or (
                abs(current_node.val - target) == abs(closest - target)
                and current_node.val < closest
            ):
                closest = current_node.val
            # move left if target is less than current node val, else right
            if target < current_node.val:
                current_node = current_node.left
            elif target > current_node.val:
                current_node = current_node.right
            else:
                return current_node.val

        return closest
