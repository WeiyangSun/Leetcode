"""
934. Shortest Bridge

You are given an nxn binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are
exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
"""

"""
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""

from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        direction_array = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y, island_cells):
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = True
            island_cells.append((x, y))
            for dx, dy in direction_array:
                dfs(x + dx, y + dy, island_cells)

        island_marker = []
        found_first = False
        for r in range(n):
            if found_first:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c, island_marker)
                    found_first = True
                    break

        queue = deque(island_marker)
        steps_taken = 0
        while queue:
            for _ in range(len(queue)): #level-size
                r, c = queue.popleft()
                for dx, dy in direction_array:
                    new_r, new_c = r + dx, c + dy
                    if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c]:
                        if grid[new_r][new_c] == 1:
                            return steps_taken
                        visited[new_r][new_c] = True
                        queue.append((new_r, new_c))
            steps_taken += 1

        return -1
