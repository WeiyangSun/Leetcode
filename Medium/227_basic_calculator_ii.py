"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the
range of [-2**31, 2**31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical
expressions, such as eval().
"""

"""
Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        last_sign = "+"
        s = s.strip() + "+"

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char in "+-*/":
                if last_sign == "+":
                    stack.append(current_num)
                elif last_sign == "-":
                    stack.append(-current_num)
                elif last_sign == "*":
                    prev = stack.pop()
                    stack.append(prev * current_num)
                elif last_sign == "/":
                    prev = stack.pop()
                    stack.append(int(prev / current_num))

                # reset for next:
                current_num = 0
                last_sign = char

        return sum(stack)
