"""
1060. Missing Element in Sorted Array

Given an integer array nums which is sorted in ascending order and all of its elements are unique and given
also an integer k, return the k-th missing number starting from the leftmost number of the array.
"""

"""
Example 1:
Input: nums = [4,7,9,10], k = 1
Output: 5

Explanation: The first missing number is 5.

Example 2:
Input: nums = [4,7,9,10], k = 3
Output: 8

Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: nums = [1,2,4], k = 3
Output: 6

Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
"""

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        full_array = set(range(nums[0], nums[-1]+k+1))
        missing = sorted(full_array - set(nums))
        return missing[k-1]


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        n = len(nums)
        if k > (nums[n-1] - nums[0] - (n-1)):
            return nums[-1] + k - (nums[n-1] - nums[0] - (n-1))

        left_pointer, right_pointer = 0, n-1
        while left_pointer < right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            if (nums[mid_pointer] - nums[0] - mid_pointer):
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer

        return nums[left_pointer - 1] + k - (nums[left_pointer] - nums[0] - left_pointer)


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def no_of_missing(i: int) -> int:
            return nums[i] - nums[0] - i

        n = len(nums)
        if k > no_of_missing(n-1):
            return nums[-1] + k - no_of_missing(n-1)

        left_pointer, right_pointer = 0, n-1
        while left_pointer < right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            if no_of_missing(mid_pointer) < k:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer

        return nums[left_pointer - 1] + k - no_of_missing(left_pointer - 1)