"""
47. Permutations II

Given a collection of numbers, `nums`, that might contain duplicates,
return all possible unique permutations in any order.
"""

"""
Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        number_case = [False] * (len(nums))

        def backtracking(current_permutation):
            if len(current_permutation) == len(nums):
                results.append(list(current_permutation))
                return

            for i in range(len(nums)):
                if number_case[i] == True:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and number_case[i - 1] == False:
                    continue

                # 1. Choose
                current_permutation.append(nums[i])
                number_case[i] = True

                # 2. Explore
                backtracking(current_permutation)

                # 3. Backtrack
                current_permutation.pop()
                number_case[i] = False

        backtracking([])
        return results
