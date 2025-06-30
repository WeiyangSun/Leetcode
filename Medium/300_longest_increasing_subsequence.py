"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence.
"""

"""
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp array holds the length of the longest increasing subsequence ending at index i
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):  # iterate through all previous elements
                # if nums[i] can extend the subsequence ending at nums[j]
                if nums[i] > nums[j]:
                    # update dp
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
