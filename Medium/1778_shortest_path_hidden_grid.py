"""
1778. Shortest Path in a Hidden Grid

This is an interactive problem.

There is a robot in a hidden grid, and you are trying to get it from its starting cell to the target
cell in this grid. The grid is of size mxn, and each cell in the grid is either empty or blocked. It
is guaranteed that the starting cell and the target cell are different, and neither of them is blocked.

You want to find the minimum distance to the target cell. However, you do not know the grid's dimensions,
the starting cell, nor the target cell. You are only allowed to ask queries to the GridMaster object.

The GridMaster class has the following functions:

- boolean canMove(char direction) Returns true if the robot can move in that direction. Otherwise, it
returns false.
- void move(char direction) Moves the robot in that direction. If this move would move the robot to a
blocked cell or off the grid, the move will be ignored, and the robot will remain in the same position.
- boolean isTarget() Returns true if the robot is currently on the target cell. Otherwise, it returns
false.

Note that direction in the above functions should be a character from {'U', 'D', 'L', 'R'}, representing
the directions up, down, left and right, respectively.

Return the minimum distance between the robot's initial starting cell and the target cell. If there is no
valid path between the cells, return -1.

Custom testing:
The test input is read as a 2D matrix grid of size m x n where:

- grid[i][j] == -1 indicates that the robot is in cell (i, j) (the starting cell).
- grid[i][j] == 0 indicates that the cell (i, j) is blocked.
- grid[i][j] == 1 indicates that the cell (i, j) is empty.
- grid[i][j] == 2 indicates that the cell (i, j) is the target cell.

There is exactly one -1 and 2 in grid. Remember that you will not have this information in your code.
"""

"""
Example 1:
Input: grid = [[1,2],[-1,0]]
Output: 2

Explanation: One possible interaction is described below:
The robot is initially standing on cell (1, 0), denoted by the -1.
- master.canMove('U') returns true.
- master.canMove('D') returns false.
- master.canMove('L') returns false.
- master.canMove('R') returns false.
- master.move('U') moves the robot to the cell (0, 0).
- master.isTarget() returns false.
- master.canMove('U') returns false.
- master.canMove('D') returns true.
- master.canMove('L') returns false.
- master.canMove('R') returns true.
- master.move('R') moves the robot to the cell (0, 1).
- master.isTarget() returns true. 
We now know that the target is the cell (0, 1), and the shortest path to the target cell is 2.

Example 2:
Input: grid = [[0,0,-1],[1,1,1],[2,0,0]]
Output: 4

Explanation: The minimum distance between the robot and the target cell is 4.

Example 3:
Input: grid = [[-1,0],[0,2]]
Output: -1

Explanation: There is no path from the robot to the target cell.
"""

from collections import deque


class Solution(object):
    def findShortestPath(self, master: "GridMaster") -> int:

        direction_array = {
            "U": (-1, 0),  # go Up - row-1
            "D": (1, 0),  # go Down - row+1
            "L": (0, -1),  # go Left - col-1
            "R": (0, 1),  # go Right - col+1
        }
        reverse_direction_array = {"U": "D", "D": "U", "L": "R", "R": "L"}

        # Use DFS to map out grid
        known_space = {(0, 0): 1}  # {(x, y): 1 empty | 2 target}
        target = None  # records (x, y) once we encounter it

        def dfs(x, y):
            nonlocal target
            if master.isTarget():
                target = (x, y)

            for d, (dx, dy) in direction_array.items():
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in known_space:
                    continue
                if master.canMove(d):
                    master.move(d)  # step forward
                    known_space[(new_x, new_y)] = 2 if master.isTarget() else 1
                    dfs(new_x, new_y)  # explore deeper
                    master.move(reverse_direction_array[d])  # perform backtracking

        dfs(0, 0)  # kick off exploration
        if target is None:
            return -1  # never met target

        # Use BFS to find shortest path
        queue = deque([(0, 0, 0)])  # (x, y, distance)
        seen = {(0, 0)}

        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == target:
                return dist
            for dx, dy in direction_array.values():
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in known_space and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    queue.append((new_x, new_y, dist + 1))

        return -1
