"""
1293. Shortest Path in a Grid with Obstacles Elimination

You are given an mxn integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0,0) to the lower right corner (m-1, n-1)
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
"""

"""
Example 1
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6

Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1

Explanation: We need to eliminate at least two obstacles to find such a walk.
"""

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)
        queue = deque([0, 0, 0, k]) #row, col, steps, remaining_eliminations
        visited = set([(0, 0, k)]) #row, col, remaining_eliminations
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]# up, down, left, right

        while queue:
            row, col, steps, remaining_eliminations = queue.popleft()
            if (row, col) == target:
                return steps

            for dir_row, dir_col in directions:
                neighbor_row, neighbor_col = row + dir_row, col + dir_col
                if 0 <= neighbor_row <= rows and 0 <= neighbor_col <= cols:
                    neighbor_elimination = remaining_eliminations - grid[neighbor_row][neighbor_col]
                    if neighbor_elimination >= 0 and (neighbor_row, neighbor_col, neighbor_elimination) not in visited:
                        visited.add((neighbor_row, neighbor_col, neighbor_elimination))
                        queue.append((neighbor_row, neighbor_col, steps + 1, neighbor_elimination))

        return -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        target = (rows-1, cols-1)
        queue = deque([(0, 0, 0, k)]) #row, col, steps, elimination_left
        visited = set([(0, 0, k)]) #row, col, elimination_left
        direction_array = [(-1,0), (1,0), (0,1), (0,-1)]

        while queue:
            row, col, steps, elimnation_left = queue.popleft()
            if (row, col, elimnation_left) in visited or elimnation_left < 0:
                continue
            if (row, col) == target:
                return steps

            visited.add((row, col, elimnation_left))
            if grid[row][col] == 1:
                elimnation_left -= 1

            for dx, dy in direction_array:
                new_row, new_col = row+dx, col+dy
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    queue.append((new_row, new_col, steps+1, elimnation_left))

        return -1