"""
907. Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every
(contiguous) subarray of arr. Since the answer may be large, return the answer
modulo 10**9 + 7.
"""

"""
Example 1:
Input: arr = [3,1,2,4]
Output: 17

Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
"""

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Core Logic:     end →
                    0   1   2   3
        start ↓   ┌─────────────────┐
        0         │ 3   1   1   1   │
        1         │     1   1   1   │
        2         │         2   2   │
        3         │             4   │
                  └─────────────────┘
        """

        MOD = 10**9 + 7
        n = len(arr)

        # left band: stretches leftwards until it meets a smaller number
        left = [0] * n  # resets to 1 when it encounters a smaller number to the left
        stack = []  # stores indices whose values are increasing

        # goes from left to right
        for idx, val in enumerate(arr):
            # pop until top of stack is smaller than val
            while stack and arr[stack[-1]] > val:
                stack.pop()
            left[idx] = idx - stack[-1] if stack else idx + 1
            stack.append(idx)  # current index becomes new top

        # right band: stretches rightwards until it meets a smaller or equal number
        right = [0] * n  # resets to 1 when it encounters a smaller number to the right
        stack.clear()

        # goes from right to left
        for idx in range(n - 1, -1, -1):
            # pop until top of stack is smaller than arr[idx]
            while stack and arr[stack[-1]] >= arr[idx]:
                stack.pop()
            right[idx] = stack[-1] - idx if stack else n - idx
            stack.append(idx)

        # adding each element's contribution
        # arr_val * left * right
        ans = 0
        for idx, val in enumerate(arr):
            ans += val * left[idx] * right[idx]
        return ans % MOD
