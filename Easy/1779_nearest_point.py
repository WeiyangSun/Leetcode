"""
1779. Find Nearest Point That Has the Same X or Y Coordinate

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). 
You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). 
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. 
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
"""

"""
Example 1:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] 
have the smallest Manhattan distance from your current location, with a distance of 1. 
[2,4] has the smallest index, so return 2.

Example 2:
Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Example 3:
Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.
"""

"""
Constraints:

1 <= points.length <= 104
points[i].length == 2
1 <= x, y, ai, bi <= 104
"""


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list(list(int))) -> int:
        """
        Examples:
            # Example 1: Nearest point with the same X coordinate
            >>> s = Solution()
            >>> s.nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2,3], [4,4]])
            2

            # Example 2: Nearest point with the same Y coordinate
            >>> s.nearestValidPoint(3, 4, [[3, 4]])
            0

            # Example 3: No valid points
            >>> s.nearestValidPoint(3, 4, [[2,3]])
            -1
        """
        min_dist, ans = float("inf"), -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:  # Valid if it shares the same X or Y as your location
                cal_dist = abs(a - x) + abs(b - y)
                if cal_dist < min_dist:
                    min_dist, ans = cal_dist, i
        return ans
