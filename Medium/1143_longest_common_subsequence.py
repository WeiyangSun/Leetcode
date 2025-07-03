"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

"""
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  

Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3

Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0

Explanation: There is no such common subsequence, so the result is 0.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        # create dp array
        dp_array = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):  # for each character in text1
            for j in range(n):  # for each character in text2
                if text1[i] == text2[j]:  # if both characters match, increment diagonal value
                    dp_array[i + 1][j + 1] = dp_array[i][j] + 1
                else:
                    dp_array[i + 1][j + 1] = max(dp_array[i][j + 1], dp_array[i + 1][j])

        return dp_array[m][n]
