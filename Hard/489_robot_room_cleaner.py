"""
489. Robot Room Cleaner

You are controlling a robot that is located somewhere in a room. The room is modeled as an mxn binary
grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have
access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The
robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the
current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
        boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
    void turnLeft();
    void turnRight();

  // Clean the current cell.
    void clean();
}

Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are
all surrounded by a wall.

Custom testing:
The input is only given to initialize the room and the robot's position internally. You must solve this problem
"blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the
room layout and the initial robot's position.
"""

"""
Example 1:
Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
Output: Robot cleaned all rooms.

Explanation: All grids in the room are marked by either 0 or 1. 0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3. From the top left corner, its position is one row below
and three columns right.

Example 2:
Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms.
"""

class Solution:
    def cleanRoom(self, robot):

        direction_array = [(-1,0), (0,1), (1,0), (0,-1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(x, y, direction_facing): #direction_facing is the current_direction (0: up, 1: right, 2: down, 3: left)
            robot.clean()
            visited.add((x, y))

            #this for loop methodology forces the robot to always be turning right in order to try next direction
            for i in range(4):
                new_direction_idx = (direction_facing + i) % 4 # %4 is the wrapping around mechanism
                delta_x, delta_y = direction_array[new_direction_idx]
                new_x, new_y = x+delta_x, y+delta_y

                if (new_x, new_y) not in visited:
                    if robot.move():
                        dfs(new_x, new_y, new_direction_idx)
                        go_back()
                robot.turnRight()

        dfs(0, 0, 0)