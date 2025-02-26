"""
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

"""
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        result = []
        nums.sort()

        def backtracking(start, combination):
            result.append(combination.copy())

            for i in range(start, len(nums)):
                # Skip Duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Explore
                combination.append(nums[i])
                backtracking(i + 1, combination)
                combination.pop()

        backtracking(0, [])
        return result
