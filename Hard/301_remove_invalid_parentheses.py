"""
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to
make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer
in any order.
"""

"""
Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]
"""

from typing import List
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid_string(string_expr):
            count = 0
            for char in string_expr:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = set([s])
        result = set()
        found_string = False

        while queue:
            current_str = queue.popleft()

            if is_valid_string(current_str):
                result.add(current_str)
                found_string = True

            if found_string:
                continue

            for i in range(len(current_str)):
                if current_str[i] not in ("(", ")"):
                    continue

                next_str = current_str[:i] + current_str[i + 1 :]

                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return list(result) if result else [""]
