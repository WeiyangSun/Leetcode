"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

- For example, do not use pow(x, 0.5) or x**0.5.
"""

"""
Example 1:
Input: x = 4
Output: 2

Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since we round it down to the
nearest integer, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x

        # Edge Case
        if x < 2:
            return x

        while left <= right:
            mid = (left + right) // 2
            mid_sq = mid*mid

            if mid_sq == x:
                return mid
            elif mid_sq < x:
                if (mid+1 * mid+1) > x:
                    return mid
                else:
                    left = mid+1
            else:
                right = mid-1

        return -1