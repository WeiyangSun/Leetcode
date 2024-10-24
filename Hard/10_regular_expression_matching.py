"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for
'.' and '*' where:

- '.' matches any single character.
- '*' matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
"""

"""
Example 1:
Input: s = 'aa', p = 'a'
Output: False

Explanation: 'a' does not match the entire string 'aa'.

Example 2:
Input: s = 'aa', p == 'a*'
Output: True

Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it
becomes 'aa'.

Example 3:
Input: s = 'ab', p = '.*'
Output: True

Explanation: '.*' means zero or more (*) of any character (.).
"""
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        pattern = '^' + p + '$'
        regex = re.compile(pattern)
        return bool(regex.match(s))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Base Case: If we have reached the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check if the current characters match
            first_match = (i < len(s)) and ((p[j] == s[i]) or (p[j] == '.'))

            # If there's a '*' following the current character in the pattern
            if j + 1 < len(p) and p[j + 1] == '*':

                # Option 1: Skip the '*' and preceding element
                memo[(i, j)] = dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                # Option 2: If first match, move to the next character in s
                memo[(i, j)] = first_match and dp(i+1, j+1)

            return memo[(i, j)]

        return dp(0, 0)