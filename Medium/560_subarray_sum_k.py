"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

"""
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        count = 0
        ledger = defaultdict(int)  # each entry says there have been x ways to reach this balance

        # Initializing
        ledger[0] = 1

        for num in nums:
            running_sum += num
            count += ledger[running_sum - k]  # add all matches so far
            ledger[running_sum] += 1  # record current balance

        return count
