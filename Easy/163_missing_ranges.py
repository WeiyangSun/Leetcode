"""
163. Missing Ranges

You are given an inclusive range [lower, upper] and a sorted unique integer
array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x
is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of nums is included in any of the ranges, and
each missing number is covered by one of the ranges.
"""

"""
Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]

Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]

Example 2:
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
"""

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        prev = lower - 1  # setting prev just before lower to handle lower boundary edge case

        # loop through nums and one extra iteration for the upper boundary
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1  # covers upper boundary edge case

            if (
                curr - prev >= 2
            ):  # if there is a gap between cur and prev with more than 1 difference, add range
                result.append([prev + 1, curr - 1])
            prev = curr

        return result
