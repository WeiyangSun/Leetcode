"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

A string is palindromic if it reads the same forward and backward.
A substring is a contiguous non-empty sequence of characters within a string.
"""

"""
Example 1:
Input: s = 'babad'
Output: 'bab'

Explanation: 'aba' is also a valid answer.

Example 2:
Input: s = 'cbbd'
Output: 'bb'
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        mem_dict = {}
        for i in range(len(s)):
            if s[i] in mem_dict:
                mem_dict[s[i]].append(i)
            else:
                mem_dict[s[i]] = [i]
        
        filtered_list = [i for v in mem_dict.values() if len(v) >= 2 for i in v]
        
        if not filtered_list:
            # No characters appeared more than once, so return the first character as the longest palindrome.
            return s[0]
        
        min_index = min(filtered_list)
        max_index = max(filtered_list)
        full_list = list(range(min_index, max_index + 1))
        
        no_missing_numbers = len(full_list) - len(filtered_list)
        
        if no_missing_numbers <= 1:
            return s[min_index: max_index + 1]
        
        # If the condition is not met, return the first character as a default case (or any other logic you'd prefer)
        return s[0]