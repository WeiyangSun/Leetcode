"""
698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into
k non-empty subsets whose sums are all equal.
"""

"""
Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true

Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false
"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False  # Total must be divided equally
        target_per_box = total_sum // k
        nums.sort(reverse=True)  # Biggest item first
        if nums[0] > target_per_box:
            return False  # No possible solution

        boxes = [0] * k

        def dfs(item_idx):
            if item_idx == len(nums):
                return True  # Every number has been successfully placed

            seen = set()
            for box_idx in range(k):
                if boxes[box_idx] in seen:  # Check if weight of box has been seen before
                    continue
                if boxes[box_idx] + nums[item_idx] <= target_per_box:
                    seen.add(boxes[box_idx])  # Remember weight

                    # Backtracking Mechanism
                    boxes[box_idx] += nums[item_idx]  # Choose
                    if dfs(item_idx + 1):  # Recurse/Explore
                        return True
                    boxes[box_idx] -= nums[item_idx]  # Backtrack

                if boxes[box_idx] == 0:  # if first empty box fails, others will too
                    break
            return False

        return dfs(0)
