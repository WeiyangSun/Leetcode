"""
113. Path Sum II

Given the root of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of
the node values in the path equals `targetSum`. Each path should be returned as a list of the node values,
not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no
children.
"""

"""
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: list[TreeNode], targetSum: int) -> list[list[int]]:

        result = []
        
        def backtracking(node, current_path, current_sum):

            if not node:
                return

            current_path.append(node.val)
            current_sum += node.val

            # Store Node
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append([current_path])

            # Explore
            backtracking(node.left, current_path, current_sum)
            backtracking(node.right, current_path, current_sum)

            # Pop
            current_path.pop()

        backtracking(root, [], 0)
        return result