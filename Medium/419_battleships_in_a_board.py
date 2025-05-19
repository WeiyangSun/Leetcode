"""
419. Battleships in a Board

Given an mxn matrix board where each cell is a battleship 'X' or empty '.', return the number of battleships
on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made
of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one
horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
"""

"""
Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0
"""

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        count_of_battleships = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    if (r == 0 or board[r - 1][c] != "X") and (c == 0 or board[r][c - 1] != "X"):
                        count_of_battleships += 1

        return count_of_battleships


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        rows, cols = len(board), len(board[0])
        count_of_battleships = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "X":
                    continue

                # If there's an 'X' above, it's part of a ship we've already counted
                if r > 0 and board[r - 1][c] == "X":
                    continue
                # If there's an 'X' to the left, it's also part of an existing ship
                if c > 0 and board[r][c - 1] == "X":
                    continue

                count_of_battleships += 1

        return count_of_battleships
