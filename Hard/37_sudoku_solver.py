"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly one in each of the 9 3x3 
sub-boxes of the grid.

The '.' character indicates empty cells.
"""

"""
Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in "123456789":
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = "."  # Backtrack
                    return False  # Trigger backtracking
        return True  # Puzzle solved

    def isValid(self, board, row, col, num):
        for i in range(9):
            # Check row
            if board[row][i] == num:
                return False
            # Check column
            if board[i][col] == num:
                return False
            # Check 3x3 sub-box
            block_row_index = 3 * (row // 3) + i // 3
            block_col_index = 3 * (col // 3) + i % 3
            if board[block_row_index][block_col_index] == num:
                return False
        return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by filling the empty cells.
        Modifies the board in-place.
        """
        # Data structures to keep track of the numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]  # Numbers in each row
        cols = [set() for _ in range(9)]  # Numbers in each column
        boxes = [set() for _ in range(9)]  # Numbers in each 3x3 box
        empty_cells = []  # List to store the positions of empty cells

        # Initialize the sets and collect empty cells
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    rows[i].add(num)
                    cols[j].add(num)
                    box_index = (i // 3) * 3 + (j // 3)
                    boxes[box_index].add(num)
                else:
                    empty_cells.append((i, j))

        # Backtracking function to fill the empty cells
        def backtrack(index=0):
            if index == len(empty_cells):
                return True  # All cells are filled successfully
            i, j = empty_cells[index]
            box_index = (i // 3) * 3 + (j // 3)
            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_index]:
                    # Place the number in the board
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)
                    # Move to the next empty cell
                    if backtrack(index + 1):
                        return True
                    # Backtrack if not valid
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_index].remove(num)
            return False  # Trigger backtracking

        backtrack()
