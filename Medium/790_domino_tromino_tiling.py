"""
790. Domino and Tromino Tiling

You have two types of tiles: a 2x1 domino shape and a tromino shape. You may rotate these
shapes.

Given an integer n, return the number of ways to tile an 2xn board. Since the answer may be
very large, return it modulo 10**9 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if
there are two 4-directionally adjacent cells on the board such that exactly one of the tilings
has both squares occupied by a tile.
"""

"""
Example 1:
Input: n = 3
Output: 5

Explanation: The five different ways are shown above.

Example 2:
Input: n = 1
Output: 1
"""


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        # Base Case:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            # Case A: You place one vertical domino in the last column. That leaves a full 2×(n−1) board in front of it ⇒ f[n−1] possibilities.
            # Case B: You place two horizontals “one atop the other” spanning the last two columns.  That leaves 2×(n−2) in front ⇒ f[n−2] possibilities.
            # Case C: You cover the final three columns with two L-trominoes.
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp[i - 3]) % MOD

        return dp[n]


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        # Base Case:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2*dp[i-1] + dp[i-3]) % MOD

        return dp[n]
