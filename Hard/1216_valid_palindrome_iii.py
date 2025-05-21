"""
1216. Valid Palindrome III

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most
k characters from it.
"""

"""
Example 1:
Input: s = 'abcdeca', k = 2
Output: true

Explanation: Remove 'b' and 'e' characters.

Example 2:
Input: s = "abbababa", k = 1
Output: true
"""

from functools import lru_cache


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def cost(left_pointer: int, right_pointer: int) -> int:

            # Base Case: 0 or 1 letter substring needs no deletion
            if left_pointer >= right_pointer:
                return 0

            if memo[left_pointer][right_pointer] != -1:
                return memo[left_pointer][right_pointer]

            # if we encounter matching outer letters, we recursively look at the inner chunks
            if s[left_pointer] == s[right_pointer]:
                memo[left_pointer][right_pointer] = cost(left_pointer + 1, right_pointer - 1)

            else:
                # if letters differ, then we must delete either side and pick the cheaper reminder
                cost_left = cost(left_pointer + 1, right_pointer)
                cost_right = cost(left_pointer, right_pointer - 1)
                memo[left_pointer][right_pointer] = 1 + min(cost_left, cost_right)

            return memo[left_pointer][right_pointer]

        return cost(0, n - 1) <= k


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        n = len(s)

        @lru_cache(None)
        def cost(left_pointer: int, right_pointer: int) -> int:

            # Base Case: 0 or 1 letter substring needs no deletion
            if left_pointer >= right_pointer:
                return 0

            # if we encounter matching outer letters, we recursively look at the inner chunks
            if s[left_pointer] == s[right_pointer]:
                return cost(left_pointer + 1, right_pointer - 1)

            # if letters differ, then we must delete either side and pick the cheaper reminder
            cost_left = cost(left_pointer + 1, right_pointer)
            cost_right = cost(left_pointer, right_pointer - 1)
            return 1 + min(cost_left, cost_left)

        return cost(0, n - 1) <= k
