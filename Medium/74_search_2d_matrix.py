"""
74. Search a 2D Matrix

You are given an mxn integer matrix, matrix, with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer, target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

"""
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        # Edge Case
        if not matrix or not matrix[0]:
            return False

        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])
        left_pointer, right_pointer = 0, (no_of_rows * no_of_cols) - 1

        while left_pointer <= right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2

            row = mid_pointer // no_of_cols
            col = mid_pointer % no_of_cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer - 1

        return False
