"""
1838. Frequency of the Most Frequent Element

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums
and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.
"""

"""
Example 1:
Input: nums = [1,2,4], k = 5
Output: 3

Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2

Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1
"""

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() # sort so that every later element is >= earlier

        left_pointer = 0
        current_window_total = 0
        best_window_length = 0

        for right_pointer, val in enumerate(nums):
            current_window_total += val
            
            # while sum of what we need is > what is available = shrink window
            # what_we_need = (height_of_rightmost * window_size) – sum_of_window
            while (val * (right_pointer - left_pointer + 1)) - current_window_total > k:
                current_window_total -= nums[left_pointer]
                left_pointer += 1

            # after shrinking window, we record the longest feasible window
            best_window_length = max(best_window_length, right_pointer - left_pointer + 1)

        return best_window_length