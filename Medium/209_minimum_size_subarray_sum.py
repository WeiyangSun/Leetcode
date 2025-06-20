"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

"""
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_pointer = 0
        current_sum = 0
        min_length = float('inf')

        for right_pointer in range(len(nums)):
            # add the current element to current_sum
            current_sum += nums[right_pointer]

            while current_sum >= target: #while current_sum is greater than or equal to target
                # updating min_length with the smaller value between current and new window size
                min_length = min(min_length, right_pointer - left_pointer + 1)
                # subtract left most element from current sum
                current_sum -= nums[left_pointer]
                left_pointer += 1

        return min_length if min_length != float('inf') else 0