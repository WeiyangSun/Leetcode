"""
149. Max Points on a Line

Given an array of points where points[i] = [x_i, y_i] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.
"""

"""
Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
"""

from typing import List, Tuple
from collections import defaultdict
from math import gcd  # to reduce coordinates to it's base


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        if n <= 2:  # 0, 1 and 2 points are always collinear
            return n

        global_max = 0

        # For each point, we will use it as the anchor point first
        for anchor_idx in range(n):
            anchor_x, anchor_y = points[anchor_idx]
            slopes = defaultdict(int)
            duplicate_points = 0
            local_max = 0

            # Compare anchor with all other points:
            for relative_idx in range(anchor_idx + 1, n):
                relative_x, relative_y = points[relative_idx]

                # In the event that there are duplicate points, we skip it
                if relative_x == anchor_x and relative_y == anchor_y:
                    duplicate_points += 1
                    continue

                # Computing reducing dx, dy pairs
                dy = relative_y - anchor_y
                dx = relative_x - anchor_x
                base = gcd(dy, dx)  # largest number to divide both deltas
                dy //= base
                dx //= base

                # Keeping sign convention
                if dx == 0:
                    dy = 1 # all verticals are changed into the same point
                elif dy == 0:
                    dx = 1 # all horizontals are changed into the same point
                else:
                    if dx < 0: # make the dx always non-negative
                        dy = -dy
                        dx = -dx

                slopes[(dy, dx)] += 1
                # most points having same angle so far
                local_max = max(local_max, slopes[(dy, dx)])

            # Update global answer: adding anchors and duplicates
            global_max = max(global_max, local_max + duplicate_points + 1)
        return global_max
