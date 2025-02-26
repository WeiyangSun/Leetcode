"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            result = target - nums[i]
            for j in range(len(nums) - 1, i, -1):
                if nums[j] == result:
                    return [i, j]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(nums)):
            dict[target - nums[i]] = dict.get(target - nums[i], i)
            if nums[i] in dict and i != dict[nums[i]]:
                return [i, dict[nums[i]]]


sol = Solution()
print(sol.twoSum(nums=[-3, 4, 3, 90], target=0))


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in nums[i + 1 :]:
                return [i, nums.index(remaining, i + 1)]
        return []


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in dict:
                return [dict[remaining], i]
            dict[v] = i
        return []


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
