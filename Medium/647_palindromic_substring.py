"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

"""
Example 1:
Input: s = "abc"
Output: 3

Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6

Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = 0

        for center in range(len(s)):

            # odd-length palindrome
            odd_count = 0
            left_pointer, right_pointer = center, center
            while (
                left_pointer >= 0
                and right_pointer < len(s)
                and s[left_pointer] == s[right_pointer]
            ):
                odd_count += 1
                left_pointer -= 1
                right_pointer += 1

            # even-length palindrome
            even_count = 0
            left_pointer, right_pointer = center, center + 1
            while (
                left_pointer >= 0
                and right_pointer < len(s)
                and s[left_pointer] == s[right_pointer]
            ):
                even_count += 1
                left_pointer -= 1
                right_pointer += 1

            total_palindromes += even_count + odd_count

        return total_palindromes


class Solution:
    def countSubstrings(self, s: str) -> int:

        def expansionFromCenter(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        total_palindrome_count = 0
        for center in range(len(s)):
            odd_palindrome = expansionFromCenter(center, center)
            even_palindrome = expansionFromCenter(center, center + 1)
            total_palindrome_count += odd_palindrome + even_palindrome
        return total_palindrome_count


class Solution:
    @staticmethod
    def expansionFromCenter(s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count

    def countSubstrings(self, s: str) -> int:

        total_palindrome_count = 0
        for center in range(len(s)):
            total_palindrome_count += Solution.expansionFromCenter(s, center, center)  # odd
            total_palindrome_count += Solution.expansionFromCenter(s, center, center + 1)  # even
        return total_palindrome_count
