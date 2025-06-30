"""
2099. Find Subsequence of Length K with the Largest Sum

You are given an integer array nums and an integer k. You want to find a
subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.
"""

"""
Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]

Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]

Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]

Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
"""

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # get a list of (index, nums)
        indexed_nums = list(enumerate(nums))
        # sort by descending nums
        indexed_nums.sort(key=lambda x: x[1], reverse=True)
        # take the indices of the top k elements
        indices = [idx for idx, _ in indexed_nums[:k]]
        indices.sort()
        return [nums[idx] for idx in indices]
