"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing (increasing)
order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

"""
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def search_binary(nums, target, find_first):

            index = -1
            left_pointer, right_pointer = 0, len(nums) - 1

            while left_pointer <= right_pointer:
                mid_pointer = left_pointer + (right_pointer - left_pointer) // 2

                if nums[mid_pointer] == target:
                    index = mid_pointer

                    if find_first:
                        right_pointer = mid_pointer - 1
                    else:
                        left_pointer = mid_pointer + 1

                elif nums[mid_pointer] < target:
                    left_pointer = mid_pointer + 1
                else:
                    right_pointer = mid_pointer - 1

            return index

        first_index = search_binary(nums, target, True)
        second_index = search_binary(nums, target, False)
        return [first_index, second_index]


sol = Solution()
print(sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
