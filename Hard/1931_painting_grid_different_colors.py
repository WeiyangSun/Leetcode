"""
1931. Painting a Grid with Three Different Colors

You are given two integers m and n. Consider an mxn grid where each cell is initially white. You can paint
each cell red, green or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the
answer can be very large, return it modulo 10**9 + 7.
"""

"""
Example 1:
Input: m = 1, n = 1
Output: 3

Explanation: The three possible colorings are shown in the image above.

Example 2:
Input: m = 1, n = 2
Output: 6

Explanation: The six possible colorings are shown in the image above.

Example 3:
Input: m = 5, n = 5
Output: 580986
"""


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        MOD = 10**9 + 7

        # Generate all vertically legal column patterns
        patterns = []  # used to store all different color combinations for a column

        def backtrack(row, prev_color, curr_recipe):
            # Base Case: all cells are filled
            if row == m:
                patterns.append(tuple(curr_recipe))
                return
            for color in range(3):
                if color != prev_color:  # new color can't match that used in previous cell
                    backtrack(
                        row + 1, color, curr_recipe + [color]
                    )  # paint cell chosen cell and go one row deeper

        backtrack(0, -1, [])  # -1 is just a dummy so any first color is allowed
        total_possible_patterns = len(
            patterns
        )  # the number of different possible color combinations for a column

        # Build Adjacency Compatibility List (ensure columns do not have the same colors across)
        compatible_patterns = [[] for _ in range(S)]
        for prev_col in range(
            total_possible_patterns
        ):  # compatible_patterns[prev_col] will hold all the idx in which curr_col is compatible
            for curr_col in range(total_possible_patterns):
                if all(patterns[prev_col][row] != patterns[curr_col][row] for row in range(m)):
                    compatible_patterns[prev_col].append(curr_col)

        # DP over columns
        curr_state = [1] * total_possible_patterns  # row of counters where one counter per pattern
        for _ in range(1, n):  # for each new column position
            new_state = [0] * total_possible_patterns
            for curr_col in range(
                total_possible_patterns
            ):  # every pattern that could be on the left
                if curr_state[curr_col]:  # there are dp[i] ways the grid could end with pattern i
                    for next_col in compatible_patterns[
                        curr_col
                    ]:  # for every such way, we are allowed to place the compatible patterns to the right
                        new_state[next_col] = (
                            new_state[next_col] + curr_state[curr_col]
                        ) % MOD  # new[j] represents the number of ways to go from i to j
            curr_state = new_state  # finished tallying for current position, so it replaces the older dp state
        return sum(curr_state) % MOD
