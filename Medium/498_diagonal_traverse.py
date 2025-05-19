"""
498. Diagonal Traverse

Given an mxn matrix mat, return an array of all the elements of the array in a diagonal order.
"""

"""
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        direction_flag = 1  # 1 means up-right; -1 means down-left
        curr_row, curr_col = 0, 0

        for _ in range(rows * cols):
            result.append(mat[curr_row][curr_col])

            # Next coordinates based on direction flag
            # Remember: Up-Right = Row - 1; Col + 1
            next_row, next_col = curr_row + (-1 if direction_flag == 1 else 1), curr_col + (
                1 if direction_flag == 1 else -1
            )

            # Up to the right
            if direction_flag == 1:
                if next_row < 0 and next_col <= cols - 1:
                    curr_row, curr_col = 0, next_col
                    direction_flag = -1
                elif next_col > cols - 1:
                    curr_row, curr_col = curr_row + 1, cols - 1
                    direction_flag = -1
                else:
                    curr_row, curr_col = next_row, next_col

            # Down to the left
            else:
                if next_col < 0 and next_row <= rows - 1:
                    curr_row, curr_col = next_row, 0
                    direction_flag = 1
                elif next_row > rows - 1:
                    curr_row, curr_col = rows - 1, curr_col + 1
                    direction_flag = 1
                else:
                    curr_row, curr_col = next_row, next_col

        return result
