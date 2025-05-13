"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if
you can flip at most k 0's.
"""

"""
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Explanation: [1,1,1,0,0,1,1,1,1,1,1]
                        -         -
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10

Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
                      - -       -
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left_pointer = 0
        no_of_k_used = 0
        max_num_of_1s = 0

        # naturally expands window to the right
        for right_pointer, val in enumerate(nums):
            if val == 0:
                no_of_k_used += 1

            # shrink window to the right if you have already used up all Ks
            while no_of_k_used > k:
                if nums[left_pointer] == 0:
                    no_of_k_used -= 1
                left_pointer += 1

            max_num_of_1s = max(max_num_of_1s, right_pointer - left_pointer + 1)

        return max_num_of_1s
