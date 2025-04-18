"""
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which
equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""

"""
Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3

Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbxit
raxbbit
rabxbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5

Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
baxgxxx
baxxxxg
bxxxxag
xxbxxag
xxxxbag
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)

        dp_array = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m + 1):
            dp_array[i][0] = 1

        for i in range(1, m+1):
            for j in range( 1, n+1):
                if s[i-1] == t[j-1]:
                    dp_array[i][j] = dp_array[i-1][j-1] + dp_array[i-1][j]
                else:
                    dp_array[i][j] = dp_array[i-1][j]

        return dp_array[m][n]