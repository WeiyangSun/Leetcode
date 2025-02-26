"""
72. Edit Distance

Given two strings `word1` and `word2`, return the minimum number of operations required to convert
`word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
"""

"""
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3

Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Lengths of the given words
        n, m = len(word1), len(word2)

        # Create a 2D DP array with dimensions (n+1) x (m+1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Initialize the first row and the first column
        for i in range(n + 1):
            dp[i][0] = i  # i deletions to transform word1[:i] to empty word
        for j in range(m + 1):
            dp[0][j] = j  # j insertions to transform empty word to word2[:j]

        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, so no additional cost
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Characters differ, consider insert, delete, or replace
                    dp[i][j] = 1 + min(
                        dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]  # Insert  # Delete  # Replace
                    )

        # The answer is the cost to transform all of word1 into word2
        return dp[n][m]
