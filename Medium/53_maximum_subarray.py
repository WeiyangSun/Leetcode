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

class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        n = len(nums)
        current_max = nums[0]
        
        for i in range(1, n):
            current_max = max(current_max, current_max + nums[i])

        return current_max

#[-2,1,-3,"4,-1,2,1",-5,4]
sol = Solution()
print(sol.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))