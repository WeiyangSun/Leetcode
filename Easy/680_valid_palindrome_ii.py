"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at
most one character from it.
"""

"""
Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true

Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(left_pointer, right_pointer):
            while left_pointer < right_pointer:
                if s[left_pointer] != s[right_pointer]:
                    return False
                left_pointer += 1
                right_pointer -= 1
            return True

        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] == s[right_pointer]:
                left_pointer += 1
                right_pointer -= 1
            else:
                return is_palindrome(left_pointer + 1, right_pointer) or is_palindrome(
                    left_pointer, right_pointer - 1
                )
        return True
