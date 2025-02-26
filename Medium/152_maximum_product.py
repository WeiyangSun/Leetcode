"""
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""

"""
Example 1:
Input: nums = [2,3,-2,4]
Output: 6

Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0

Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

"""
Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


# Cubic Solution
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        global_max = float("-inf")

        for i in range(n):
            for j in range(i, n):
                local_max = 1
                for k in range(i, j + 1):
                    local_max *= nums[k]

                if local_max > global_max:
                    global_max = local_max

        return global_max


# Quadratic Solution
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        global_max = float("-inf")

        for i in range(n):
            local_max = 1
            for j in range(i, n):
                local_max *= nums[j]

                if local_max > global_max:
                    global_max = local_max

        return global_max


# Linear Solution
class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        n = len(nums)
        local_max, local_min, global_max = nums[0], nums[0], nums[0]

        for i in range(1, n):

            if nums[i] < 0:
                local_max, local_min = local_min, local_max

            local_max = max(nums[i], local_max * nums[i])
            local_min = min(nums[i], local_min * nums[i])

            global_max = max(global_max, local_max)

        return global_max
