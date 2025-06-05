"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. The indices of
the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one
will explode. If both are the same size, both will explode. Two asteroids are moving in the same
direction will never meet.
"""

"""
Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]

Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []

Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]

Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # iterate through each asteroid in the input list
        for asteroid in asteroids:
            alive_flag = True  # assume current asteroid has not exploded
            # process collisions only if the current asteroid is moving left (negative)
            while alive_flag and stack and asteroid < 0 < stack[-1]:
                # if right moving asteroid is smaller, it explodes (pop)
                if stack[-1] < -asteroid:
                    stack.pop()
                # elif both asteroids are the same size, both explode
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive_flag = False
                # else right moving asteroid is larger, current asteroid explodes
                else:
                    alive_flag = False

            if alive_flag:
                stack.append(asteroid)

        return stack
