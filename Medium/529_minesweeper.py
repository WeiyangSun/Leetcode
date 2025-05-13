"""
529. Minesweeper

You are given an mxn char matrix board representing the game board where:

- 'M' represents an unrevealed mine,
- 'E' represents an unrevealed empty square,
- 'B' represents a blank square that has no adjacent mines (i.e. above, below, left, right, and all 4 diagonals),
- digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
- 'X' represents a revealed mine.

You are also given an integer array click where click = [click_row, click_col] represents the next click position among
all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

- If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
- If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent
unrevealed squares should be revealed recursively.
- If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing
the number of adjacent mines.
- Return the board when no more squares will be revealed.
"""

"""
Example 1:
Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Example 2:
Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
"""

from typing import List
from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        direction_array = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        click_row, click_col = click
        if board[click_row][click_col] == "M":
            board[click_row][click_col] = "X"
            return board

        rows, cols = len(board), len(board[0])
        queue = deque([(click_row, click_col)])

        while queue:
            board_row, board_col = queue.popleft()
            if board[board_row][board_col] != "E":
                continue

            # Checks if neighbors of current location has mines
            neighboring_mines = 0
            for dir_x, dir_y in direction_array:
                row_new, col_new = board_row + dir_x, board_col + dir_y
                if 0 <= row_new < rows and 0 <= col_new < cols:
                    if board[row_new][col_new] == "M":
                        neighboring_mines += 1

            # If there are mines, put a str representing number of mines
            if neighboring_mines:
                board[board_row][board_col] = str(neighboring_mines)
            # Else, it is a blank space and needs to put neighbors into queues
            else:
                board[board_row][board_col] = "B"
                for dir_x, dir_y in direction_array:
                    row_new, col_new = board_row + dir_x, board_col + dir_y
                    if 0 <= row_new < rows and 0 <= col_new < cols:
                        if board[row_new][col_new] == "E":
                            queue.append((row_new, col_new))

        return board


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        direction_array = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        click_row, click_col = click
        if board[click_row][click_col] == "M":
            board[click_row][click_col] = "X"
            return board

        rows, cols = len(board), len(board[0])
        queue = deque([(click_row, click_col)])

        while queue:
            board_row, board_col = queue.popleft()
            if board[board_row][board_col] != "E":
                continue

            # Checks if neighbors of current location has mines
            neighboring_mines = sum(
                1
                for dir_x, dir_y in direction_array
                if 0 <= board_row + dir_x < rows
                and 0 <= board_col + dir_y < cols
                and board[board_row + dir_x][board_col + dir_y] == "M"
            )

            # If there are mines, put a str representing number of mines
            if neighboring_mines:
                board[board_row][board_col] = str(neighboring_mines)
            # Else, it is a blank space and needs to put neighbors into queues
            else:
                board[board_row][board_col] = "B"
                for dir_x, dir_y in direction_array:
                    row_new, col_new = board_row + dir_x, board_col + dir_y
                    if (
                        0 <= row_new < rows
                        and 0 <= col_new < cols
                        and board[row_new][col_new] == "E"
                    ):
                        queue.append((row_new, col_new))

        return board


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        direction_array = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        click_row, click_col = click
        if board[click_row][click_col] == "M":
            board[click_row][click_col] = "X"
            return board

        rows, cols = len(board), len(board[0])
        queue = deque([(click_row, click_col)])

        while queue:
            board_row, board_col = queue.popleft()
            if board[board_row][board_col] != "E":
                continue

            def counting_neighboring_mines(row: int, col: int) -> int:

                return sum(
                    1
                    for dir_x, dir_y in direction_array
                    if 0 <= row + dir_x < rows
                    and 0 <= col + dir_y < cols
                    and board[row + dir_x][col + dir_y] == "M"
                )

            # Checks if neighbors of current location has mines
            neighboring_mines = counting_neighboring_mines(board_row, board_col)

            # If there are mines, put a str representing number of mines
            if neighboring_mines:
                board[board_row][board_col] = str(neighboring_mines)
            # Else, it is a blank space and needs to put neighbors into queues
            else:
                board[board_row][board_col] = "B"
                for dir_x, dir_y in direction_array:
                    row_new, col_new = board_row + dir_x, board_col + dir_y
                    if (
                        0 <= row_new < rows
                        and 0 <= col_new < cols
                        and board[row_new][col_new] == "E"
                    ):
                        queue.append((row_new, col_new))

        return board
