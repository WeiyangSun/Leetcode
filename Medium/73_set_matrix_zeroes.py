"""
73. Set Matrix Zeroes

Given an mxn integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

"""
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Edge Case - Empty Matrix
        if not matrix or not matrix[0]:
            return

        n_rows, n_cols = len(matrix), len(matrix[0])
        # Flags to check if first row or column has zeroes
        first_row_has_zero = any(matrix[0][col] == 0 for col in range(n_cols))
        first_col_has_zero = any(matrix[row][0] == 0 for row in range(n_rows))

        # First pass - Mark zeros in the first row/column
        for row in range(1, n_rows):
            for col in range(1, n_cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Second pass - Mark entire row or column to 0
        for row in range(1, n_rows):
            for col in range(1, n_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Third pass - Handling First Row
        if first_row_has_zero:
            for col in range(n_cols):
                matrix[0][col] = 0
        # Handling First Column
        if first_col_has_zero:
            for row in range(n_rows):
                matrix[row][0] = 0
