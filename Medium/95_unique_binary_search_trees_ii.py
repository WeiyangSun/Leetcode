"""
95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique binary search trees (BST), which has exactly n
nodes of unique values from 1 to n. Return the answer in any order.
"""

"""
Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> [[TreeNode]]:
        
        if n == 0:
            return []
        
        memo = {}
        
        def buildTrees(start, end):
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for i in range(start, end+1):
                # Generate left sub-trees
                left_subtrees = buildTrees(start, i-1)
                
                # Generate right sub-trees
                right_subtrees = buildTrees(i+1, end)
                
                # Combine each left and right subtree with root
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                
            memo[(start, end)] = all_trees
            return all_trees
        
        return buildTrees(1, n)