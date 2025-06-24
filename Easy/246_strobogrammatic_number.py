"""
246. Strobogrammatic Number

Given a string num which represents an integer, return true if num is
a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated
180 degrees (looked at upside down).
"""

"""
Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic_pairs = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        left_pointer, right_pointer = 0, len(num) - 1

        while left_pointer <= right_pointer:
            left_char, right_char = num[left_pointer], num[right_pointer]

            if (
                left_char not in strobogrammatic_pairs
                or strobogrammatic_pairs[left_char] != right_char
            ):
                return False

            left_pointer += 1
            right_pointer -= 1

        return True
