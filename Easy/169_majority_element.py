"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋
times. You may assume that the majority element always exists in the array.
"""

"""
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        # requires O(n) runtime and O(n) memory
        return max(nums_counter.keys(), key=nums_counter.get)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # requires O(n) runtime and O(1) memory
        majority_candidate = None  # keep track of current candidate for majority element
        majority_candidate_count = 0

        for num in nums:
            if majority_candidate_count == 0:
                majority_candidate = num
            if num == majority_candidate:
                majority_candidate_count += 1
            else:
                # each time when you encounter a new number, you downvote current majority
                # this "weakens" the majority candidate
                majority_candidate_count -= 1

        return majority_candidate
