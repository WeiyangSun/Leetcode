"""
64. Minimum Path Sum

Given a mxn grid filled with non-negative numbers, find a path from top left to bottom right, which
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

"""
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7

Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        no_of_rows = len(grid)
        no_of_cols = len(grid[0])
        dp = [[0] * no_of_cols for _ in range(no_of_rows)]

        # Setting Base Case
        dp[0][0] = grid[0][0]

        # Setting Top Row
        for col in range(1, no_of_cols):
            dp[0][col] = dp[0][col - 1] + grid[0][col]
        # Setting Left Col
        for row in range(1, no_of_rows):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for row in range(1, no_of_rows):
            for col in range(1, no_of_cols):
                dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])

        return dp[no_of_rows - 1][no_of_cols - 1]
