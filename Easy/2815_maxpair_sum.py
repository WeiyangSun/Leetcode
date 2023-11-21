"""
2815. Max Pair Sum in an Array

You are given a 0-indexed integer array nums.
You have to find the maximum sum of a pair of numbers 
from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.
"""

"""
Example 1:
Input: nums = [51,71,17,24,42]
Output: 88

Explanation: 
For i = 1 and j = 2, nums[i] and nums[j] have equal maximum
digits with a pair sum of 71 + 17 = 88. 
For i = 3 and j = 4, nums[i] and nums[j] have equal maximum
digits with a pair sum of 24 + 42 = 66.
It can be shown that there are no other pairs with equal maximum
digits, so the answer is 88.

Example 2:
Input: nums = [1,2,3,4]
Output: -1

Explanation: No pair exists in nums with equal maximum digits.
"""

"""
Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 104
"""

class Solution:
    def maxSum(self, nums: list(int)) -> int:
        total_len = len(nums)
        ans = -1
        for i_pointer in range(total_len):
            for j_pointer in range(i_pointer+1, total_len):
                sum = nums[i_pointer] + nums[j_pointer]
                if sum < 100 and sum > 10:
                    if (str(sum)[0] == str(sum)[-1]) and sum > ans:
                        ans = sum
        return ans

from collections import defaultdict

class Solution:
    def maxSum(self, nums: list(int)) -> int:
        max_by_digit = defaultdict(int)
        max_sum = -1

        for num in nums:
            digit = max(str(num))

            if digit in max_by_digit:
                max_sum = max(max_sum, max_by_digit[digit] + num)

            max_by_digit[digit] = max(max_by_digit[digit], num)

        return max_sum