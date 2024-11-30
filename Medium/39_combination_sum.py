"""
39. Combination Sum

Given an array of distinct integers `candidates` and a target integer `target`,
return a list of all unique combinations of `candidates` where the chosen
numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

The test cases are generated such that the number of unique combinations
that sum up to `target` is less than `150` combinations for the given input.
"""

"""
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, current_combination, current_sum):
            # Base Success Case:
            if current_sum == target:
                result.append(list(current_combination))
                return
            # Base Failure Case:
            if current_sum > target:
                return
            
            # BackTracking
            for i in range(start, len(candidates)):
                # 1. Choose
                current_combination.append(candidates[i])
                # 2. Explore
                backtrack(i, current_combination, current_sum + candidates[i])
                # 3. Backtrack
                current_combination.pop()

        backtrack(0, [], 0)
        return result

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, current_combination, remaining_sum):
            #Base Success Case:
            if remaining_sum == 0:
                result.append(current_combination.copy())
                return

            #Base Failure Case:
            if remaining_sum < 0:
                return

            #Backtracking
            for i in range(start, len(candidates)):
                #1. Choose
                current_combination.append(candidates[i])
                #2. Explore
                backtrack(i, current_combination, remaining_sum-candidates[i])
                #3. Backtrack
                current_combination.pop()

        backtrack(0, [], target)
        return result
            