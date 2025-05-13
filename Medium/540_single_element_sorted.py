"""
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except
for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

"""
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left_pointer, right_pointer = 0, len(nums) - 1

        while left_pointer < right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            # align mid to the first element in a pair (even-index)
            if mid_pointer % 2 == 1:
                mid_pointer -= 1

            # if the pair starting at the mid is valid, single element is to the right
            if nums[mid_pointer] == nums[mid_pointer + 1]:
                left_pointer = mid_pointer + 2  # skips over entire pair
            # else, single element is to the left
            else:
                right_pointer = mid_pointer

        return nums[left_pointer]
