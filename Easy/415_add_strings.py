"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling
large integers (such as BigInteger). You must also not convert the inputs to
integers directly.
"""

"""
Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        num1_pointer, num2_pointer = len(num1) - 1, len(num2) - 1

        while num1_pointer >= 0 or num2_pointer >= 0 or carry:
            x = int(num1[num1_pointer]) if num1_pointer >= 0 else 0
            y = int(num2[num2_pointer]) if num2_pointer >= 0 else 0

            total = x + y + carry
            result.append(str(total % 10))
            carry = total // 10
            num1_pointer -= 1
            num2_pointer -= 1

        return "".join(result[::-1])
