"""
496. Next Greater Element I

The next greater element of some element x in an array is the first greater
element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1
is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2. If there is no next
greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater
element as described above.
"""

"""
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
    the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the
    answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]

Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the
answer is -1.
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dictionary to hold the next greatest value for each element in nums2
        next_greater = {}
        # stack to keep indices of nums2 elements for each next greater that has not been found
        stack = []

        for num in nums2:
            # while stack is not empty and current number is greater than top element in stack
            while stack and num > stack[-1]:
                prev_num = stack.pop()
                next_greater[prev_num] = num
            stack.append(num)

        # for elements left in the stack, there is no next greater element
        for num in stack:
            next_greater[num] = -1  # assign -1

        result = []
        for num in nums1:
            result.append(next_greater[num])

        return result
