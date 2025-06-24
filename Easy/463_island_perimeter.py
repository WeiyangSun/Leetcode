"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The
grid is completely surrounded by water, and there is exactly one island
(i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected
to the water around the island. One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the
perimeter of the island.
"""

"""
Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for each_row in range(rows):
            for each_col in range(cols):
                if grid[each_row][each_col] == 1:
                    perimeter += 4
                    # check if it is possible that row above has an island
                    if each_row > 0 and grid[each_row - 1][each_col] == 1:
                        perimeter -= 2
                    # check if it is possible that col to the left is an island
                    if each_col > 0 and grid[each_row][each_col - 1] == 1:
                        perimeter -= 2

        return perimeter
