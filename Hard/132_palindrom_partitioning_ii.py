"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
"""

"""
Example 1:
Input: s = "aab"
Output: 1

Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1
"""

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        is_palindrome_dp = [[False]*n for _ in range(n)]

        for center in range(n):
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                is_palindrome_dp[left][right] = True
                left -= 1
                right += 1
            left, right = center, center+1
            while left >= 0 and right < n and s[left] == s[right]:
                is_palindrome_dp[left][right] = True
                left -= 1
                right += 1

        cuts_dp = [0]*n
        for end in range(n):
            cuts_dp[end] = end
            for start in range(end+1):
                if is_palindrome_dp[start][end] == True:
                    if start == 0:
                        cuts_dp[end] = 0
                        break
                    else:
                        cuts_dp[end] = min(cuts_dp[end], cuts_dp[start-1] +1)
        return cuts_dp[-1]

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        is_palindrome_dp = [[False]*n for _ in range(n)]
        cuts_dp = [0]*n

        for end in range(n):
            min_cut = end
            for start in range(end+1):
                if s[start] == s[end] and (end-start <= 1 or is_palindrome_dp[start+1][end-1]):
                    is_palindrome_dp[start][end] = True
                    min_cut = 0 if end == 0 else min(min_cut, cuts_dp[end-1]+1)
            cuts_dp[end] = min_cut
        return cuts_dp[-1]