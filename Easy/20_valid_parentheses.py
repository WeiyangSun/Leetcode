"""
20. Valid Parentheses

Given a string 's' containing just the characters '(', ')', '{', '}', '[', and ']', determine
if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""

"""
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        open_parentheses_map = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in open_parentheses_map.keys():
                stack.append(open_parentheses_map.get(char))
            else:
                # If stack is empty or character doesn't match stack pop
                if not stack or char != stack.pop():
                    return False

        return not stack


sol = Solution()
print(sol.isValid(s="([)]"))
