"""
852. Peak Index in a Mountain Array

You are given an integer mountain array arr of length n where the values
increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.
"""

"""
Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left_pointer, right_pointer = 0, len(arr) - 1

        while left_pointer < right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2

            if arr[mid_pointer] < arr[mid_pointer + 1]:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer

        return left_pointer
