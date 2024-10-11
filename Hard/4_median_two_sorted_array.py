"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).
"""

"""
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2

Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5

Explanation: merged array = [1,2,3,4] and median is (2+3)/2 = 2.5.
"""
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged_list = []
        pointer_1, pointer_2 = 0, 0
        
        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] <= nums2[pointer_2]:
                merged_list.append(nums1[pointer_1])
                pointer_1 += 1
            else:
                merged_list.append(nums2[pointer_2])
                pointer_2 += 1
        
        while pointer_1 < len(nums1):
            merged_list.append(nums1[pointer_1])
            pointer_1 += 1
        
        while pointer_2 < len(nums2):
            merged_list.append(nums2[pointer_2])
            pointer_2 += 1
            
        # Median Logic
        n = len(merged_list)
        if n % 2 == 1:
            median = merged_list[n // 2]
        else:
            median = (merged_list[n // 2 - 1] + merged_list[n // 2]) / 2
            
        return median