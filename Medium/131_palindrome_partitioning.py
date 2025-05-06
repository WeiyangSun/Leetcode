"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible
palindrome partitioning of s.
"""

"""
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)

        dp = [[False]*n for _ in range(n)]
        for right in range(n):
            for left in range(right+1):
                if s[left] == s[right] and (right - left <= 1 or dp[left+1][right-1]):
                    dp[left][right] = True

        #DFS with backtracking
        result, path = [], []
        def dfs(start: int) -> None:
            if start == n:
                result.append(path.copy())
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    dfs(end + 1)
                    path.pop()
        dfs(0)
        return result