"""
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of
contiguous subarrays where the product of all the elements in the subarray
is strictly less than k.
"""

"""
Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8

Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly
less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  # if k is less than or equal to 1, no product can be strictly less than k
            return 0

        product = 1
        left_pointer = 0
        result_counter = 0

        for right_pointer in range(len(nums)):
            product *= nums[right_pointer]

            while product >= k:
                product //= nums[left_pointer]
                left_pointer += 1

            result_counter += right_pointer - left_pointer + 1

        return result_counter
