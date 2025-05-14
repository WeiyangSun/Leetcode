"""
2962. Count Subarrays Where Max Element Appears at Least K times

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that
subarray.

A subarray is a contiguous sequence of elements within an array.
"""

"""
Example 1:
Input: nums = [1,3,2,3,3], k = 2
Output: 6

Explanation: The subarrays that contain the element 3 at least 2 times are:
[1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:
Input: nums = [1,4,2,1], k = 3
Output: 0

Explanation: No subarray contains the element 4 at least 3 times.
"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        right_pointer = 0
        result = 0

        for left_pointer, _ in enumerate(nums):
            right_pointer = max(right_pointer, left_pointer)
            count = nums[left_pointer: right_pointer].count(max_num)

            while right_pointer < len(nums) and count < k:
                if nums[right_pointer] == max_num:
                    count += 1
                right_pointer += 1

            if count == k:
                result += len(nums) - right_pointer + 1
        return result


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        left_pointer = 0
        result, count = 0, 0

        for right_pointer, val in enumerate(nums):
            if val == max_num:
                count += 1

            while count >= k:
                #since condition is at least k, therefore any extension becomes valid
                result += len(nums) - right_pointer 
                if nums[left_pointer] == max_num:
                    count -= 1
                left_pointer += 1

        return result