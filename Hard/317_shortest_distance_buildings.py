"""
317. Shortest Distance from All Buildings

You are given an m x n grid of values 0, 1, or 2, where:

- each 0 marks an empty land that you can pass by freely,
- each 1 marks a building that you cannot pass through, and
- each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings
in the shortest total travel distance. You can only move up, down, left,
and right.

Return the shortest travel distance for such a house. If it is not possible
to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of
the friends and the meeting point.
"""

"""
Example 1:
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel
distance of 3+3+1=7 is minimal. So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1
"""

from typing import List
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # Base Case - empty grid case
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        # sum of distances to each empty land
        dist = [[0] * cols for _ in range(rows)]
        # number of buildings that can be reached by a cell
        reach = [[0] * cols for _ in range(rows)]

        total_buildings = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Launch BFS from every building
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:  # found a building
                    total_buildings += 1

                    queue = deque([(row, col, 0)])  # row, col and distance so far
                    seen = [[False] * cols for _ in range(rows)]
                    seen[row][col] = True

                    while queue:
                        curr_row, curr_col, curr_dist = queue.popleft()

                        for d_row, d_col in directions:
                            new_row, new_col = curr_row + d_row, curr_col + d_col

                            if (
                                0 <= new_row < rows
                                and 0 <= new_col < cols
                                and not seen[new_row][new_col]
                                and grid[new_row][new_col] == 0
                            ):
                                seen[new_row][new_col] = True
                                dist[new_row][new_col] += curr_dist + 1
                                reach[new_row][new_col] += 1
                                queue.append((new_row, new_col, curr_dist + 1))

        # Choosing the best square
        if total_buildings == 0:
            return -1  # no buildings at all

        shortest_travel_distance = float("inf")
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and reach[row][col] == total_buildings:
                    shortest_travel_distance = min(shortest_travel_distance, dist[row][col])

        return shortest_travel_distance if shortest_travel_distance != float("inf") else -1
