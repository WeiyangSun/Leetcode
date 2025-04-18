"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
"""

"""
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

"""
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_sum = int(a, 2) + int(b, 2)
        return bin(int_sum)[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum_count = carry
            if i >= 0:
                sum_count += ord(a[i]) - ord("0")
            if j >= 0:
                sum_count += ord(b[j]) - ord("0")
            i, j = i - 1, j - 1
            carry = 1 if sum_count > 1 else 0
            res += str(sum_count % 2)

        if carry != 0:
            res += str(carry)
        return res[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            first_binary_digit = int(a[i]) if i >= 0 else 0
            second_binary_digit = int(b[j]) if j >= 0 else 0

            # summation
            sum = first_binary_digit + second_binary_digit + carry

            result.append(str(sum % 2))
            carry = sum // 2

            i -= 1
            j -= 1

        return "".join(result[::-1])
