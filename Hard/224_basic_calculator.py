"""
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return
the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expression,
such as eval().
"""

"""
Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # used to remember outer results and signs when we enter '('
        last_sign = 1  # used to determine whether number should be added or subtracted from total
        current_num = 0  # stores digits that we are currently reading
        running_total = 0  # keeps track of how much we have evaluated

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # handles multi-digit
            elif char in "+-":
                running_total += last_sign * current_num
                current_num = 0
                last_sign = 1 if char == "+" else -1
            elif char == "(":
                # pushed to stack to pause this mathematical operation
                stack.append((running_total, last_sign))
                # resets and prepare for upcoming mathematical operation
                running_total, last_sign = 0, 1
            elif char == ")":
                # performs evaluation between what is read and what has been evaluated
                running_total += last_sign * current_num
                current_num = 0
                # unpauses previous mathematical operation
                outer_result, outer_sign = stack.pop()
                running_total = outer_result + outer_sign * running_total

        return running_total + last_sign * current_num  # adding in last pending number
