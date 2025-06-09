"""
633. Sum of Square Numbers

Given a non-negative integers c, decide whether there're two integers a and b such that
a**2 + b**2 = c.
"""

"""
Example 1:
Input: c = 5
Output: true

Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left_pointer = 0
        right_pointer = int(c**0.5)

        while left_pointer <= right_pointer:
            current = left_pointer**2 + right_pointer**2

            if current == c:
                return True
            elif current < c:
                left_pointer += 1
            else:
                right_pointer -= 1

        return False