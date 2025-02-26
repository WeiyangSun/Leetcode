"""
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's
and return its area.
"""

"""
Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 6

Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1
"""


class Solution:

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        # heights array to store histogram heights are each row
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    heights[c] = 0
                else:
                    heights[c] += 1

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        # Finding largest rectangle in histogram
        stack = []
        max_area = 0
        extended_heights = heights + [0]

        for ix, h in enumerate(extended_heights):

            while stack and extended_heights[stack[-1]] > h:
                current_height = extended_heights[stack.pop()]
                current_width = ix if not stack else ix - stack[-1] - 1

                max_area = max(max_area, current_height * current_width)

            stack.append(ix)

        return max_area
