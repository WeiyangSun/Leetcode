"""
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.
"""

"""
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0]) if rows else 0

        def dfs(row, col, ix):
            # If we have matched all letters in the word
            if ix == len(word):
                return True

            # Boundary Conditions:
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[ix]:
                return False

            # Temporarily mark cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Exploring Neighbors
            found = (
                dfs(row + 1, col, ix + 1)
                or dfs(row - 1, col, ix + 1)
                or dfs(row, col + 1, ix + 1)
                or dfs(row, col - 1, ix + 1)
            )

            # Restore Original Value
            board[row][col] = temp

            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
