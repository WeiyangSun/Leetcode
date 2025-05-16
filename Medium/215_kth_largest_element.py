"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the k-th largest element in the
array.

Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

Can you solve it without sorting?
"""

"""
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k

        def quick_select(left, right):
            # Choose random pivot
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            # By always moving the pivot to the end first, the code doesn’t have to special-case
            # skipping over the pivot during the partition-loop
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            quickselect_store = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[quickselect_store], nums[i] = nums[i], nums[quickselect_store]
                    quickselect_store += 1
            nums[quickselect_store], nums[right] = nums[right], nums[quickselect_store]

            if quickselect_store == target_idx:
                return nums[quickselect_store]
            elif quickselect_store < target_idx:
                return quick_select(quickselect_store + 1, right)
            else:
                return quick_select(left, quickselect_store - 1)

        return quick_select(0, len(nums) - 1)


import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for x in nums:
            heapq.heappush(min_heap, x)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k

        def quickSelect(left, right):
            pivot_val = nums[right]
            low_pointer = left
            high_pointer = right

            while low_pointer <= high_pointer:
                while low_pointer <= high_pointer and nums[low_pointer] < pivot_val:
                    low_pointer += 1
                while low_pointer <= high_pointer and nums[high_pointer] > pivot_val:
                    high_pointer -= 1
                if low_pointer <= high_pointer:
                    nums[low_pointer], nums[high_pointer] = nums[high_pointer], nums[low_pointer]
                    low_pointer += 1
                    high_pointer -= 1

            if target_idx <= high_pointer:
                return quickSelect(left, high_pointer)
            elif target_idx >= low_pointer:
                return quickSelect(low_pointer, right)
            else:
                return nums[k]

        return quickSelect(0, len(nums) - 1)
