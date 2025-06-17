"""
974. Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays
that have a sum divisible by k.

A subarray is a contiguous part of an array.
"""

"""
Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7

Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0
"""

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total_subarray = 0
        prefix_sum = 0  # running sum of elements seen
        freq_count = {0: 1}  # represents bucket-label - how many times seen
        # seeded with 0 -> 1 for dummy row

        # Core logic:
        # A = denominator*numerator₁ + remainder
        # B = denominator*numerator₂ + remainder
        # A − B = (denominator*numerator₁ + remainder) − (denominator*numerator₂ + remainder)
        # A - B =  denominator * (numerator₁ − numerator₂) ← a whole-number multiple of denominator
        for num in nums:
            prefix_sum += num  # update running sum
            remainder = prefix_sum % k  # forms bucket label

            # any earlier prefix with same remainder forms a valid sub-array
            total_subarray += freq_count.get(remainder, 0)
            freq_count[remainder] = freq_count.get(remainder, 0) + 1  # increment count to record

        return total_subarray
