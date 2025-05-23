"""
282. Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary
operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target
value.

Note that operands in the returned expressions should not contain leading zeros.
"""

"""
Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []

Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
"""

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtracking(idx, expr, total, last_num_added):
            if idx == len(num):
                if total == target:
                    result.append(expr)
                return

            for cut in range(idx, len(num)):
                if cut > idx and num[idx] == "0":
                    break  # forbid numbers with leading '0's

                slice_str = num[idx : cut + 1]
                slice_val = int(slice_str)

                if idx == 0:
                    # starting slice: place without an operator
                    backtracking(cut + 1, slice_str, slice_val, slice_val)
                else:
                    # try "+"
                    backtracking(cut + 1, expr + "+" + slice_str, total + slice_val, slice_val)
                    # try "-"
                    backtracking(cut + 1, expr + "-" + slice_str, total - slice_val, -slice_val)
                    # try "*"
                    backtracking(
                        cut + 1,
                        expr + "*" + slice_str,
                        total - last_num_added + last_num_added * slice_val,
                        last_num_added * slice_val,
                    )

        backtracking(0, "", 0, 0)
        return result
