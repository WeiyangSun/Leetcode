"""
778. Swim in Rising Water

You are given an nxn integer matrix grid where each value grid[i][j] represents the elevation at that point
(i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim
infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n-1, n-1) if you start at the top left square
(0, 0).
"""

"""
Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3

Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16

Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
"""

from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]  # get elevation, x and y
        max_elevation = 0
        target = (n - 1, n - 1)

        direction_array = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            elevation, x, y = heapq.heappop(heap)
            max_elevation = max(max_elevation, elevation)
            if (x, y) == target:
                return max_elevation
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for delta_x, delta_y in direction_array:
                new_x, new_y = x + delta_x, y + delta_y
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                    heapq.heappush(heap, (grid[new_x][new_y], new_x, new_y))

        return -1
