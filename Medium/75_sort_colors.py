"""
75. Sort Colors

Given an array nums, with n objects colored red, white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors in the order of red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

"""
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Triple Pointer Solution
        # Everything before low is guaranteed 0
        # Everything after high is guaranteed 2
        # Mid is the exploration
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Do not move mid forward because the number that was swapped might be a 2, 1 or 0. Need to check again
                # This is not needed for nums[mid] == 0 because everything before nums[low] is guaranteed to be 0.
