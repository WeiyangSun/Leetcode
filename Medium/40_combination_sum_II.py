"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates, where the candidate
numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

"""
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()
        result = []

        def backtracking(start, current_combination, remaining_target):
            # Base Success Case
            if remaining_target == 0:
                result.append(current_combination.copy())
                return

            # Base Failure Case
            if remaining_target < 0:
                return

            prev = -1
            # Backtracking
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                # 1. Choose
                current_combination.append(candidates[i])
                # 2. Explore
                backtracking(i + 1, current_combination, remaining_target - candidates[i])
                # 3. Backtrack
                current_combination.pop()
                prev = candidates[i]

        backtracking(0, [], target)
        return result
