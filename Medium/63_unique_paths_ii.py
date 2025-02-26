"""
63. Unique Paths II

You are given an mxn integer array grid. There is a robot initially located at the top-left corner
(i.e. grid[0][0]). The robot tries to move to the bottom-right corner (i.e. grid[m-1][n-1]). The robot
can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot
include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2*10^9.
"""

"""
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2

Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        no_of_rows = len(obstacleGrid)
        no_of_cols = len(obstacleGrid[0])

        if obstacleGrid[no_of_rows - 1][no_of_cols - 1] == 1:
            return 0

        dp = [[0] * no_of_cols for _ in range(no_of_rows)]

        # Base Case
        dp[0][0] = 1

        # Top Row
        for col in range(1, no_of_cols):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col - 1]
            else:
                dp[0][col] = 0

        # Left Column
        for row in range(1, no_of_rows):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]
            else:
                dp[row][0] = 0

        # Filling the rest of DP array
        for row in range(1, no_of_rows):
            for col in range(1, no_of_cols):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[no_of_rows - 1][no_of_cols - 1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If the end cell is blocked, return 0 immediately
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # dp array of size n (for columns)
        dp = [0] * n

        # Initialize dp[0] if start cell is not blocked
        dp[0] = 1

        # Fill the dp array row by row
        for i in range(m):
            for j in range(n):
                # If there is an obstacle, ways = 0
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    # If not an obstacle and j > 0, add the ways from left (dp[j-1])
                    if j > 0:
                        dp[j] += dp[j - 1]

                # dp[j] at the end of this iteration
                # represents number of ways to reach (i, j)

        return dp[n - 1]
