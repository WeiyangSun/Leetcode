"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

"""
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1

Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

"""
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

#Cubic Solution
class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        n = len(nums)
        global_max = float('-inf')

        for i in range(n):
            for j in range(i, n):
                local_max = 0
                for k in range(i, j+1):
                    local_max += nums[k]
            
                if local_max > global_max:
                    global_max = local_max
        
        return global_max

# Quadratic Solution
class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        n = len(nums)
        global_max = float('-inf')
        
        for i in range(n):
            local_max = 0
            for j in range(i, n):
                local_max += nums[j]
            
                if local_max > global_max:
                    global_max = local_max

        return global_max

# Linear Solution
class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        n = len(nums)
        local_max, global_max = nums[0], nums[0]

        for i in range(1, n):
            local_max = max(nums[i], local_max + nums[i])
            if local_max > global_max:
                global_max = local_max
        
        return global_max


sol = Solution()
print(sol.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))