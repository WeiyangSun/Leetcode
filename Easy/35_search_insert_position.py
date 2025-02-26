"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return
the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

"""
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left_pointer, right_pointer = 0, len(nums) - 1

        while left_pointer <= right_pointer:
            mid_pointer = left_pointer + (right_pointer - left_pointer) // 2

            if nums[mid_pointer] == target:
                return mid_pointer

            elif nums[mid_pointer] < target:
                left_pointer = mid_pointer + 1

            else:
                right_pointer = mid_pointer - 1

        return left_pointer


sol = Solution()
print(sol.searchInsert(nums=[1, 3, 5, 6], target=3))
