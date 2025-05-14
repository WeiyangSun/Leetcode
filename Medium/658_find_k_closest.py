"""
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in
the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b
"""

"""
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
"""

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left_pointer, right_pointer = 0, len(arr) - k

        while left_pointer < right_pointer:
            mid_point = (left_pointer + right_pointer) // 2
            if x - arr[mid_point] > arr[mid_point + k] - x:
                left_pointer = mid_point + 1
            else:
                right_pointer = mid_point

        return arr[left_pointer: left_pointer+k]