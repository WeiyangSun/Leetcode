"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.
"""

"""
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)  # empty list to store results

        # core logic: think of this as a convex problem
        left_pointer, right_pointer = 0, len(nums) - 1
        # Fill result backwards
        for i in range(len(nums) - 1, -1, -1):
            left_sq = nums[left_pointer] ** 2
            right_sq = nums[right_pointer] ** 2
            # compare squared values
            if left_sq > right_sq:
                # place into results at i-index
                result[i] = left_sq
                left_pointer += 1
            else:
                result[i] = right_sq
                right_pointer -= 1

        return result
