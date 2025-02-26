"""
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area
"""

"""
Example 1:
| 1 | 0 | 1 | 0 | 0 |
        ------------
| 1 | 0 ||1 ||1|| 1||
| 1 | 1 ||1 ||1|| 1||
        -------------
| 1 | 0 | 0 | 1 | 0 |
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
    -----
| 0 ||1||
---------
||1|| 0 |
-----
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
| 0 |
Input: matrix = [["0"]]
Output: 0
"""

"""
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""


class BruteForceSolution:
    def maximalSquare(self, matrix: list(list(str))) -> int:
        result = 0
        for i in range(len(matrix)):  # row-wise
            for j in range(len(matrix[0])):  # column-wise
                curr = 0  # current length of square at (i,j)
                flag = True  # indicates a valid square still exists
                while flag:
                    for k in range(curr + 1):
                        if (
                            i < curr
                            or j < curr
                            or matrix[i - curr][j - k] == "0"
                            or matrix[i - k][j - curr] == "0"
                        ):
                            flag = False
                            break
                    curr += flag
                if curr > result:  # new maximum length of square obtained
                    result = curr

        return result * result


class TopDownSolution:
    def maximalSquare(self, matrix: list(list(str))) -> int:
        # recursive - top down
        rows, cols = len(matrix), len(matrix[0])
        cache = {}  # map each position in cache (row, col) to maxLength of square possible

        # Time Complexity: O(mn) Memory Complexity: O(mn)
        def recursive_helper(row, col):
            # Base Case: Out of Bounds Cpnditions
            if row >= rows or col >= cols:
                return 0
            # Check if value is stored in cache
            if (row, col) not in cache:
                down = recursive_helper(row + 1, col)
                right = recursive_helper(row, col + 1)
                diag = recursive_helper(row + 1, col + 1)

                # Initial value of maxArea at location is set to 0
                cache[(row, col)] = 0
                # Since input is a str
                if matrix[row][col] == "1":
                    cache[(row, col)] = 1 + min(down, right, diag)

            return cache[(row, col)]

        recursive_helper(0, 0)
        length_list = cache.values()  # getting list of maxLength
        return max(length_list) ** 2


class BottomUpSolution:
    def maximalSquare(self, matrix: list(list(str))) -> int:
        # Base Case:
        if matrix is None or len(matrix) < 1 or len(matrix[0]) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp_matrix[i + 1][j + 1] = (
                        min(dp_matrix[i][j], dp_matrix[i + 1][j], dp_matrix[i][j + 1]) + 1
                    )

        max_length = max(map(max, dp_matrix))
        return max_length * max_length
