"""
329. Longest Increasing Path in a Matrix

Given an mxn integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move
diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

"""
Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4

Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4

Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1
"""

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memoization_cache = [[0] * cols for _ in range(rows)]
        direction_array = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # DFS helper function
        def dfs(row, col):
            if memoization_cache[row][col] != 0:
                return memoization_cache[row][col]

            max_path = 1
            for delta_row, delta_col in direction_array:
                new_row, new_col = row + delta_row, col + delta_col
                if (
                    (0 <= new_row < rows)
                    and (0 <= new_col < cols)
                    and (matrix[new_row][new_col] > matrix[row][col])
                ):
                    length = 1 + dfs(new_row, new_col)
                    max_path = max(max_path, length)
            memoization_cache[row][col] = max_path
            return max_path

        # Executing Workflow
        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))  # try starting from each cell

        return result
