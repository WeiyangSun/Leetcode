"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

"""
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = []
        
        def backtracking(start, current_subset):
            # Record current_subset
            results.append(list(current_subset))
        
            for i in range(start, len(nums)):
                # Choose
                current_subset.append(nums[i])
                # Explore
                backtracking(i+1, current_subset)
                # Backtrack
                current_subset.pop()
        
        backtracking(0, [])
        return results
            