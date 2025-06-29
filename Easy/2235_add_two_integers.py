"""
2235. Add Two Integers

Given two integers num1 and num2, return the sum of the two integers.
"""

"""
Example 1:
Input: num1 = 12, num2 = 5
Output: 17

Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

Example 2:
Input: num1 = -10, num2 = 4
Output: -6

Explanation: num1 + num2 = -6, so -6 is returned.
"""

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # bitwise XOR ('^') to add without carrying
        # bitwise AND ('&') and left shift to compute carry

        while num2 != 0:
            # carry now contains common set bits of num1 and num2
            carry = num1 & num2
            # num1 contains sum bits, ignoring carry
            num1 = num1 ^ num2
            # num2 now contains carry bits, shifted to left
            num2 = carry << 1

        return num1