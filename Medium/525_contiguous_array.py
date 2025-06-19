"""
525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous
subarray with an equal number of 0 and 1.
"""

"""
Example 1:
Input: nums = [0,1]
Output: 2

Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0
and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2

Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number
of 0 and 1.

Example 3:
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6

Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0
and 1.
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        running_sum = 0
        max_array_length = 0
        first_seen_map = {0: -1}  # initialized with 0 at index -1 {balance: index}

        for idx, num in enumerate(nums):
            # update running sum -> step forward on 1 and step backwards on 0
            running_sum = +1 if num == 1 else -1

            if running_sum in first_seen_map:
                current_length = idx - first_seen_map[running_sum]
                max_array_length = max(max_array_length, current_length)
            else:
                first_seen_map[running_sum] = idx

        return max_array_length
