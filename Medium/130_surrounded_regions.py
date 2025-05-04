"""
130. Surrounded Regions

You are given an mxn matrix board containing letters 'X' and 'O', capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every '0' cell.
- Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of
the region cells are on the edge of the board.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not
need to return anything.
"""

"""
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the
board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
"""

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Edge Cases
        if not board or not board[0]:
            return

        nRows, nCols = len(board), len(board[0])

        def flooding_mechanism(row: int, col: int) -> None:
            # Case where flooding is not supposed to happen
            if row < 0 or row >= nRows or col < 0 or col >= nCols or board[row][col] != '0':
                return

            # Case where flooding is supposed to happen
            board[row][col] = 'S'
            flooding_mechanism(row+1, col)
            flooding_mechanism(row-1, col)
            flooding_mechanism(row, col+1)
            flooding_mechanism(row, col-1)

        # Start from Edges First
        for row in range(nRows):
            flooding_mechanism(row, 0)
            flooding_mechanism(row, nCols - 1)
        for col in range(nCols):
            flooding_mechanism(0, col)
            flooding_mechanism(nRows - 1, col)

        # Flip back S to O's
        for row in range(nRows):
            for col in range(nCols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'