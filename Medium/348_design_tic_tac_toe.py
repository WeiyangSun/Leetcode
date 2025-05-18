"""
348. Design Tic-Tac-Toe

Assume the following rules are for the tic-tac-toe game on an nxn board between two players:

1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal
row wins the game.

Implement the TicTacToe class:

- TicTacToe(int n) Initializes the object the size of the board n.
- int move(int row, int col, int player) Indicates that the player with id player plays at the
cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players
alternate in making moves. Return

    - 0 if there is no winner after the move,
    - 1 if player 1 is the winner after the move, or
    - 2 if player 2 is the winner after the move
"""

"""
Example 1:
Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
"""


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows_counter = [0] * n
        self.cols_counter = [0] * n
        self.diag_counter = 0
        self.anti_diag_counter = 0

    def move(self, row: int, col: int, player: int) -> int:
        mark = 1 if player == 1 else -1

        # Updating Rows and Columns Counter
        self.rows_counter[row] += mark
        self.cols_counter[col] += mark

        # Updating diagonals
        if row == col:
            self.diag_counter += mark
        if row + col == self.n - 1:
            self.anti_diag_counter += mark

        # Check if move wins the game
        if (
            abs(self.rows_counter[row]) == self.n
            or abs(self.cols_counter[col]) == self.n
            or abs(self.diag_counter) == self.n
            or abs(self.anti_diag_counter) == self.n
        ):
            return player

        return 0


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        # 2-D array to track
        self.rows_counter = [[0] * n for _ in range(2)]
        self.cols_counter = [[0] * n for _ in range(2)]
        self.diag_counter = [0, 0]
        self.anti_diag_counter = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        player_no = player - 1  # 0-indexed

        # Update Counters
        self.rows_counter[player_no][row] += 1
        self.cols_counter[player_no][col] += 1
        if row == col:
            self.diag_counter[player_no] += 1
        if row + col == (self.n - 1):
            self.anti_diag_counter[player_no] += 1

        # Win Conditions
        if (
            self.rows_counter[player_no][row] == self.n
            or self.cols_counter[player_no][col] == self.n
            or self.diag_counter[player_no] == self.n
            or self.anti_diag_counter[player_no] == self.n
        ):
            return player

        return 0
