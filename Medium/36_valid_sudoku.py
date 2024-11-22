"""
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to
be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition
2. Each column must contain the digits 1-9 without repetition
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits
1-9 without repetition

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
- Only the filled cells need to be validated according to the mentioned
rules.
"""

"""
Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

from collections import Counter

class Solution:
    def isValidSudoku(self, board: list[list[int]]) -> bool:
        
        # Check each row for no duplicate values
        for row in board:
            row_count = Counter(row)
            if any(v > 1 for k, v in row_count.items() if k != '.'):
                return False
        
        # Check each col for no duplicate values
        transpose_board = [list(i) for i in zip(*board)]
        for col in transpose_board:
            col_count = Counter(col)
            if any(v > 1 for k, v in col_count.items() if k != '.'):
                return False
        
        # Check 3x3 square
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                flatten_square = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        flatten_square.append(board[x][y])
                
                value_count = Counter(flatten_square)
                if any(v > 1 for k,v in value_count.items() if k != '.'):
                    return False

        return True


class Solution:
    def isValidSudoku(self, board:list[list[int]]) -> bool:
        
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        
        #Iterate through cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num != '.':
                    block_index = (i // 3) * 3 + j // 3
                    
                    if (num in rows[i] or num in columns[j] or num in blocks[block_index]):
                        return False
                    
                    rows[i].add(num)
                    columns[j].add(num)
                    blocks[block_index].add(num)

        return True