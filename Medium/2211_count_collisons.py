"""
2211. Count Collisons on a Road

There are n cars on an infinitely long road.
The cars are numbered from 0 to n - 1 from left to right
and each car is present at a unique point.

You are given a 0-indexed string directions of length n.
Directions[i] can be either 'L', 'R', or 'S' denoting 
whether the ith car is moving towards the left, towards 
the right, or staying at its current point respectively.
Each moving car has the same speed.

The number of collisions can be calculated as follows:

When two cars moving in opposite directions collide with each other,
the number of collisions increases by 2.
When a moving car collides with a stationary car, the number of
collisions increases by 1.
After a collision, the cars involved can no longer move and
will stay at the point where they collided. Other than that,
cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.
"""

"""
Example 1:
Input: directions = "RLRSLL"
Output: 5

Explanation:
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. 
Since they are moving in opposite directions, 
the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other.
Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other.
Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other.
After car 4 collides with car 3, it will stay at
the point of collision and get hit by car 5.
The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5. 

Example 2:
Input: directions = "LLRR"
Output: 0

Explanation:
No cars will collide with each other. Thus, the
total number of collisions that will happen on the road is 0.
"""

"""
Constraints:

1 <= directions.length <= 105
directions[i] is either 'L', 'R', or 'S'.
"""


class Solution:
    def countCollisions(self, directions: str) -> int:

        n = len(directions)
        result, i, carsFromRight = 0, 0, 0

        # Resolves Base Case where vehicles all turn left - No collisions
        while i < n and directions[i] == "L":
            i += 1

        # Normal Operations
        while i < n:
            if directions[i] == "R":
                carsFromRight += 1
            else:
                result += carsFromRight if directions[i] == "S" else carsFromRight + 1
                carsFromRight = 0
            i += 1

        return result


import collections


class Solution:
    def alternate_countCollisons(self, directions: str) -> int:
        car_queue = collections.deque(list(directions))

        # Note: Trying to combine both while loops into a single while loop isn't runtime efficient
        # It seems like it is better to perform one task per loop

        # Handles the edge case - Where all vehicles turn L
        while len(car_queue) > 0 and car_queue[0] == "L":
            car_queue.popleft()

        # Handles the edge case - Where all vehicles turn R
        while len(car_queue) > 0 and car_queue[-1] == "R":
            car_queue.pop()

        # Ultimately, as long as you perform a turn inside, you will get a collision -  except for stationary
        return len(car_queue) - car_queue.count("S")
