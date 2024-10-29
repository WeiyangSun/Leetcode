"""
16. Three Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that
the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

"""
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums:list[int], target:int) -> int:
        nums.sort()
        closest_value = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n-2):
            
            left_pointer = i + 1
            right_pointer = n - 1

            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]

                if abs(current_sum - target) < abs(closest_value - target):
                    closest_value = current_sum

                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return closest_value

sol = Solution()
print(sol.threeSumClosest(nums=[-1,2,1,-4], target=1))
