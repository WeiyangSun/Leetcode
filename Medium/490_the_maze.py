"""
490. The Maze

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go
through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the mxn maze, the ball's start position and the destination, where start = [start_row, start_col] and
destination = [destination_row, destination_col], return True if the ball can stop at the destination, otherwise
return False.

You may assume that the borders of the maze are all walls (see examples).
"""

"""
Example 1:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false

Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.

Example 3:
Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
"""

from typing import List
from collections import deque


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        rows, cols = len(maze), len(maze[0])
        direction_array = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque([tuple(start)])

        while queue:
            curr_row, curr_col = queue.popleft() # picking the next station to start
            if (curr_row, curr_col) == tuple(destination):
                return True

            if (curr_row, curr_col) in visited:
                continue # skipping if already explored
            visited.add((curr_row, curr_col)) # marking as explored

            for delta_row, delta_col in direction_array:
                new_row, new_col = curr_row, curr_col # start rolling from current cell
                while (
                    0 <= new_row + delta_row < rows
                    and 0 <= new_col + delta_col < cols
                    and maze[new_row + delta_row][new_col + delta_col] == 0
                ): # making sure to stay inside the grid and that the next square is empty
                    new_row += delta_row # keep sliding
                    new_col += delta_col

                # after the loop when the ball has hit a wall
                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col)) # enqueue this position for next move

        return False # queue has been exhausted - no path
