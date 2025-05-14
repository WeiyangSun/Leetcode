"""
159. Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest substring that contains at most two distinct
characters.
"""

"""
Example 1:
Input: s = "eceba"
Output: 3

Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5

Explanation: The substring is "aabbb" which its length is 5.
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counts = defaultdict(int)
        left_pointer = 0
        max_length = 0

        for right_pointer, char in enumerate(s):
            counts[char] += 1

            while len(counts) > 2:
                counts[s[left_pointer]] -= 1
                if counts[s[left_pointer]] == 0:
                    del counts[s[left_pointer]]
                left_pointer += 1

            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length
