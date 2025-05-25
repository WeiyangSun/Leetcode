"""
827. Making A Large Island

You are given an nxn binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
"""

"""
Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3

Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4

Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4

Explanation: Can't change any 0 to 1, only one island with area = 4.
"""

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2  # 0 is water, 1 is unvisited island
        labels = [[0] * n for _ in range(n)]
        direction_array = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(row, col, island_id):
            if not (0 <= row < n and 0 <= col < n) or grid[row][col] != 1 or labels[row][col] != 0:
                return 0
            labels[row][col] = island_id
            area = 1
            for delta_row, delta_col in direction_array:
                area += dfs(row + delta_row, col + delta_col)
            return area

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and labels[i][j] == 0:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        max_area = max(island_sizes.values(), default=0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    area = 1
                    for delta_row, delta_col in direction_array:
                        new_row, new_col = i + delta_row, j + delta_col
                        if 0 <= new_row < n and 0 <= new_col < n:
                            island_id = labels[new_row][new_col]
                            if island_id > 1 and island_id not in seen:
                                area += island_sizes[island_id]
                                seen.add(island_id)
                    max_area = max(max_area, area)

        return max_area if max_area > 0 else n * n
