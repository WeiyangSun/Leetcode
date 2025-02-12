"""
96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique binary search trees which has exactly n nodes
of unique values from 1 to n.
"""

"""
Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
"""

class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0]*(n+1)
        
        # Base Cases
        dp[0] = 1
        dp[1] = 1
        
        # Filling in DP
        for i in range(2, n+1):
            # Try each number as the root
            for root in range(1, i+1):
                left_trees = dp[root-1]
                right_trees = dp[i-root]
                dp[i] += left_trees * right_trees
        
        return dp[n]