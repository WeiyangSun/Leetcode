"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for
'.' and '*' where:

- '.' matches any single character.
- '*' matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
"""

"""
Example 1:
Input: s = 'aa', p = 'a'
Output: False

Explanation: 'a' does not match the entire string 'aa'.

Example 2:
Input: s = 'aa', p == 'a*'
Output: True

Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it
becomes 'aa'.

Example 3:
Input: s = 'ab', p = '.*'
Output: True

Explanation: '.*' means zero or more (*) of any character (.).
"""
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        pattern = "^" + p + "$"
        regex = re.compile(pattern)
        return bool(regex.match(s))


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Base Case: If we have reached the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check if the current characters match
            first_match = (i < len(s)) and ((p[j] == s[i]) or (p[j] == "."))

            # If there's a '*' following the current character in the pattern
            if j + 1 < len(p) and p[j + 1] == "*":

                # Option 1: Skip the '*' and preceding element
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Option 2: If first match, move to the next character in s
                memo[(i, j)] = first_match and dp(i + 1, j + 1)

            return memo[(i, j)]

        return dp(0, 0)


def isMatch(s, p):
    m, n = len(s), len(p)
    # Initialize the DP table with False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Fill dp[0][j] for patterns like a*, a*b*, a*b*c* that can match an empty string
    for j in range(2, n + 1):
        if p[j - 1] == "*" and dp[0][j - 2]:
            dp[0][j] = True

    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                # Zero occurrences of the preceding element
                dp[i][j] = dp[i][j - 2]
                # One or more occurrences of the preceding element
                if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == "." or p[j - 1] == s[i - 1]:
                # Single character match
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = False

    return dp[m][n]
