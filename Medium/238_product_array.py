"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

"""
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

"""
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        pointer_A = 0
        result = []
        while pointer_A < len(nums):
            if pointer_A == 0:
                selected_array = nums[pointer_A+1:]
            else:
                selected_array = nums[:pointer_A] + nums[pointer_A+1:]
            
            num_product = 1
            for i in selected_array:
                num_product *= i
            result.append(num_product)
            pointer_A += 1

        return result

class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        n, ans, suffix_product = len(nums), [1]*len(nums), 1
        
        for i in range(1, n):
            ans[i] = ans[i-1]*nums[i-1]
        for i in range(n-1, -1, -1):
            ans[i] *= suffix_product
            suffix_product *= nums[i]
        return ans

sol = Solution()
print(sol.productExceptSelf(nums=[1,2,3,4]))