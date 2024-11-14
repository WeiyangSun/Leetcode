"""
29. Divide Two Integers

Given two integers `dividend` and `divisor`, divde two integers without
using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its
fractional part. For example `8.345` would be truncated to `8`, and `-2.7335`
would be truncated to `-2`.

Return the quotient after dividing `dividend` by `divisor`.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [-2**31, 2**31 - 1]. FOr this problem,
if the quotient is strictly greater than 2**31 - 1, then return 2**31 - 1.
and if the quotient is strictly less than -2**31, then return -2**31.
"""

"""
Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Explanation: 7/-3 = -2.33333.. which is truncated to -2.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= temp_divisor << 1:
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            result += multiple
            
        if negative:
            result = -result
        
        return max(MIN_INT, min(MAX_INT, result))