"""
994. Rotting Oranges

You are given an mxn grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh oragne, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is
impossible, return -1.
"""

"""
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting
only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0

Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        queue = deque()  # captures row, col, minutes_elasped
        fresh_oranges_count = 0

        # initialize queue with starting rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_oranges_count += 1

        minutes_elasped = 0
        direction_array = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            curr_row, curr_col, curr_mins = queue.popleft()
            for dx, dy in direction_array:
                neighbor_row, neighbor_col = curr_row + dx, curr_col + dy
                if (
                    0 <= neighbor_row < rows
                    and 0 <= neighbor_col < cols
                    and grid[neighbor_row][neighbor_col] == 1
                ):
                    grid[neighbor_row][neighbor_col] = 2
                    fresh_oranges_count -= 1
                    queue.append((neighbor_row, neighbor_col, curr_mins + 1))
                    minutes_elasped = curr_mins + 1

        if fresh_oranges_count > 0:
            return -1

        return minutes_elasped
