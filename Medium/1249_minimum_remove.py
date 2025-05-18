"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(', ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ('(' or ')', in any positions)
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.
"""

"""
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""

Explanation: An empty string is also valid.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        initial_chars = []  # build new string with only valid parentheses
        open_count = 0

        # Perform first pass: remove any excess )
        for char in s:
            if char == "(":
                open_count += 1
                initial_chars.append(char)
            elif char == ")":
                if open_count == 0:
                    continue
                open_count -= 1
                initial_chars.append(char)
            else:
                initial_chars.append(char)

        final_chars = []
        open_to_remove = open_count

        # Perform second pass: removing unmatched (
        for char in reversed(initial_chars):
            if char == "(" and open_to_remove > 0:
                open_to_remove -= 1
                continue
            final_chars.append(char)

        return "".join(reversed(final_chars))


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []

        for ix, char in enumerate(chars):
            if char == "(":
                stack.append(ix)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    char[ix] == ""

        for ix in stack:
            chars[ix] = ""

        return "".join(chars)
