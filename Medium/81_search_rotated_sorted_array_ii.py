"""
81. Search in Rotated Sorted Array II

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
[4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false
if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

"""
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        
        left_pointer, right_pointer = 0, len(nums)-1
        
        while left_pointer <= right_pointer:
            
            mid_pointer = left_pointer + (right_pointer - left_pointer) // 2
            
            if nums[mid_pointer] == target:
                return True
            
            # Seeing which side is sorted
            if nums[left_pointer] < nums[mid_pointer]: #left-side is sorted
                if nums[left_pointer] <= target < nums[mid_pointer]:
                    right_pointer = mid_pointer - 1
                else:
                    left_pointer = mid_pointer + 1
            elif nums[mid_pointer] < nums[right_pointer]: #right-side is sorted
                if nums[mid_pointer] < target <= nums[right_pointer]:
                    left_pointer = mid_pointer + 1
                else:
                    right_pointer = mid_pointer - 1
            else: # Covers duplicate scenario
                if nums[left_pointer] == nums[mid_pointer] and nums[mid_pointer] == nums[right_pointer]:
                    left_pointer += 1
                    right_pointer -= 1
                elif nums[left_pointer] == nums[mid_pointer]:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return False


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        
        left_pointer, right_pointer = 0, len(nums)-1
        
        while left_pointer <= right_pointer:
            
            mid_pointer = left_pointer + (right_pointer - left_pointer) // 2
            
            if nums[mid_pointer] == target:
                return True
            
            if nums[left_pointer] < nums[mid_pointer]:
                if nums[left_pointer] <= target < nums[mid_pointer]:
                    right_pointer = mid_pointer - 1
                else:
                    left_pointer = mid_pointer + 1
            
            elif nums[left_pointer] > nums[mid_pointer]:
                if nums[mid_pointer] < target <= nums[right_pointer]:
                    left_pointer = mid_pointer + 1
                else:
                    right_pointer = mid_pointer - 1
            
            else:
                left_pointer += 1
    
        return False