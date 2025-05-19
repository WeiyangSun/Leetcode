"""
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

"""
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (
            n + 1
        )  # can the prefix of the string up to position i be broken into words from the dict
        dp[0] = True  # Empty string is always segmentable

        for i in range(1, n + 1):  # for every possible substring end
            for word in wordSet:  # try every word as a potential ending
                if i >= len(word) and s[i - len(word) : i] == word:
                    # if word fits and prefix can be segmented, mark as True
                    if dp[
                        i - len(word)
                    ]:  # looking backwards, you have to ensure that the prior conditions is still True
                        dp[i] = True
                        break

        return dp[n]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[i:j] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
