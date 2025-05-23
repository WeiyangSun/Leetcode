"""
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More
formally, if you are on index `i` on the current row, you may move to either
index `i` or index `i+1` on the next row.
"""

"""
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11

Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

Example 2:
Input: triangle = [[-10]]
Output: -10
"""

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        # Exception
        if not triangle:
            return 0

        # Dynamic Programming - Bottom Up starting from 2nd last row
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])

        return triangle[0][0]