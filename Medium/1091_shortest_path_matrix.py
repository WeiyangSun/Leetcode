"""
1091. Shortest Path in Binary Matrix

Given an nxn binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell
(i.e., (n-1, n-1)) such that:

- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and
they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
"""

"""
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Edge Case
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = deque([(0, 0, 1)])  # initialize with start_x, start_y and distance
        direction_array = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        grid[0][0] = 1  # shows that it has been explored

        while queue:
            row, col, dist = queue.popleft()
            # hit exit point
            if row == col == n - 1:
                return dist

            for dx, dy in direction_array:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, dist + 1))

        return -1
