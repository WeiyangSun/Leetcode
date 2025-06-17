"""
1901. Find a Peak Element II

A peak element in a 2D grid is an element that is strictly greater than all of its
adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any
peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the
value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
"""

"""
Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]

Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]

Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
"""

from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        low_row, high_row = 0, rows - 1  # search range using rows

        while low_row < high_row:
            mid_row = (low_row + high_row) // 2
            # find column of max element in mid_row
            max_col = mat[mid_row].index(max(mat[mid_row]))

            if mat[mid_row][max_col] < mat[mid_row + 1][max_col]:
                low_row = mid_row + 1
            else:
                high_row = mid_row

        # Extract Peak Col
        peak_row = low_row
        peak_col = mat[peak_row].index(max(mat[peak_row]))
        return [peak_row, peak_col]
