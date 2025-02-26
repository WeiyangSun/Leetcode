"""
18. Four Sum

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct
# nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""

"""
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early Termination as not possible to solve
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Early Continuation
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left_pointer = j + 1
                right_pointer = n - 1

                if nums[i] + nums[j] + nums[left_pointer] + nums[left_pointer + 1] > target:
                    break

                if nums[i] + nums[j] + nums[right_pointer] + nums[right_pointer - 1] < target:
                    continue

                while left_pointer < right_pointer:
                    total = nums[i] + nums[j] + nums[left_pointer] + nums[right_pointer]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left_pointer], nums[right_pointer]])

                        while (
                            left_pointer < right_pointer
                            and nums[left_pointer] == nums[left_pointer + 1]
                        ):
                            left_pointer += 1
                        while (
                            left_pointer < right_pointer
                            and nums[right_pointer] == nums[right_pointer - 1]
                        ):
                            right_pointer -= 1

                        left_pointer += 1
                        right_pointer -= 1

                    elif total < target:
                        left_pointer += 1
                    else:
                        right_pointer -= 1

        return result


sol = Solution()
print(sol.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
