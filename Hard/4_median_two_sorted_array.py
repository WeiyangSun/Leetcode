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

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        m, n = len(A), len(B)
        
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half_len = 0, m, (m+n+1)//2
        
        while imin <= imax:
            i = imin + (imax - imin) // 2 #mid-point of the smaller array
            j = half_len - i # determines how many elements in big array should be included in left partition
            
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])
                
                if (m+n)%2 == 1:
                    return max_of_left
                
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                
                return (max_of_left + min_of_right) / 2.0
            