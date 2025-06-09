"""
503. Next Greater Element II

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next
greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which
means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
"""

"""
Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]

Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [-1] * n
        stack = []  # indices waiting for a greater element

        for i in range(2 * n):  # iterate twice to imitate circular loop
            curr = nums[i % n]  # this performs correction when it goes the 2nd round

            while stack and nums[stack[-1]] < curr:
                result[stack.pop()] = curr

            # push indices from the first lap in
            if i < n:
                stack.append(i)

        return result
