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


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        if m < n:
            return self.isInterleave(s2, s1, s3)

        dp = [False]*(n+1)
        dp[0] = True

        # Iterating through s2 and updating array
        for j in range(1, n+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        # Iterating through s1 and updating array
        # Logic:
        # For each character in s1, iterate through s2 and update the dp array based on the transition rule:
        # dp[j] = (dp[j] and s1[i] == s3[i+j]) or (dp[j-1] and s2[j] == s3[i+j]).
        # The transition rule checks if the current s3[i+j] can be matched by either s1[i] or s2[j],
        # relying solely on the previous values in the dp array.
        for i in range(1, m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])

        return dp[n]