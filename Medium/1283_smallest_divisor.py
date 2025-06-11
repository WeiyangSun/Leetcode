"""
1283. Find the Smallest Divisor Given a Threshold

Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer `divisor`,
divide all the array by it , and sum the division's result. Find the smallest `divisor` such that the result
mentioned above is less than or equal to `threshold`.

Each result of the division is rounded to the nearest integer greater than or equal to that element.
(For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
"""

"""
Example 1:
Input: nums = [1,2,5,9], threshold = 6
Output: 5

Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the 
sum will be 5 (1+1+1+2). 

Example 2:
Input: nums = [44,22,33,11,1], threshold = 5
Output: 44
"""

from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def compute_sum(divisor):
            total = 0
            for num in nums:
                total += math.ceil(num / divisor)  # given a divisor, divide all num and get total
            return total

        left_pointer, right_pointer = 1, max(nums)
        result = right_pointer

        while left_pointer <= right_pointer:
            mid_pointer = (right_pointer + left_pointer) // 2
            current_sum = compute_sum(mid_pointer)
            if current_sum <= threshold:  # if mid pointer works, record it and try smaller
                result = mid_pointer
                right_pointer = mid_pointer - 1
            else:
                left_pointer = mid_pointer + 1

        return result
