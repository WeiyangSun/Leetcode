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
        
        max_palindrome = s[0]
        for indices in mem_dict.values():
            if len(indices) >= 2:
                for i in range(len(indices)):
                    for j in range(i+1, len(indices)):
                        start = indices[i]
                        end = indices[j] + 1
                        substring = s[start:end]
                        if substring == substring[::-1]:
                            if len(substring) > len(max_palindrome):
                                max_palindrome = substring
        
        return max_palindrome
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandAroundCenter(s: str, left: int, right: int) -> int:
        
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return right - left - 1
        
        if not s:
            return ""
        
        start, end = 0, 0
        
        for ix in range(len(s)):
            # Odd-Length Palindrome
            len1 = expandAroundCenter(s, ix, ix)
            # Even-Length
            len2 = expandAroundCenter(s, ix, ix + 1)
            
            max_len = max(len1, len2)
            
            if max_len > start - end:
                start = ix - (max_len - 1) // 2
                end = ix + (max_len // 2)
                
        return s[start: end + 1]
                
            