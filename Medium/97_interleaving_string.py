"""
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings
respectively, such that:

- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note a + b is the concatenation of strings a and b.
"""

"""
Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Exceptions:
        if len(s3) != (len(s1) + len(s2)):
            return False

        # Setting up 2-D DP array
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Initialization
        dp[0][0] = True

        # Filling the first row
        for col in range(1, len(s2) + 1):
            dp[0][col] = dp[0][col - 1] and s2[col - 1] == s3[col - 1]
        # Filling the first col
        for row in range(1, len(s1) + 1):
            dp[row][0] = dp[row - 1][0] and s1[row - 1] == s3[row - 1]

        # Filling the rest of the DP
        for row in range(1, len(s1) + 1):
            for col in range(1, len(s2) + 1):
                # Matching S1
                match_s1 = dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]
                # Matching S2
                match_s2 = dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                # Combining
                dp[row][col] = match_s1 or match_s2

        return dp[len(s1)][len(s2)]
