"""
670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number

Return the maximum valued number you can get.
"""

"""
Example 1:
Input: num = 2736
Output: 7236

Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973

Explanation: No swap.
"""


class Solution:
    def maximumSwap(self, nums: int) -> int:
        s = list(str(nums))  # becomes ["2", "7", "3", "6"]
        last_pos = {int(val): ix for ix, val in enumerate(s)}

        for ix, char in enumerate(s):
            current = int(char)

            for d in range(9, current, -1):
                if d in last_pos and last_pos[d] > ix:
                    j = last_pos[d]
                    s[ix], s[j] = s[j], s[ix]
                    return int("".join(s))

        return nums  # already at maximum
