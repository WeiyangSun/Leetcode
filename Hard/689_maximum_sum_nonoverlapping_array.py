"""
689. Maximum Sum of 3 Non-Overlapping Subarrays

Given an integer array nums and an integer k, find three non-overlapping
subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position
of each interval (0-indexed). If there are multiple answers, return the
lexicographically smallest one.
"""

"""
Example 1:
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]

Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
indices [0, 3, 5]. We could have also taken [2, 1], but an answer of [1, 3, 5]
would be lexicographically larger.

Example 2:
Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
"""

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # pre-compute sum of every k-length window
        window_sum = [0] * (n - k + 1)  # rolling sum
        cur_window = sum(nums[:k])
        window_sum[0] = cur_window
        for i in range(1, n - k + 1):
            # you can use a sliding window instead however it would result in O(k)
            # whereas this remains at O(1) since it is just adding and subtracting
            cur_window += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = cur_window

        # moving from left-to-right: this is the earliest index that contains the highest sum
        left_best_indices = [0] * len(window_sum)
        left_best = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[left_best]:
                left_best = i
            left_best_indices[i] = left_best

        # moving from right-to-left: this is the earliest index that contains the highest sum
        right_best_indices = [0] * len(window_sum)
        right_best = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[right_best]:
                right_best = i
            right_best_indices[i] = right_best

        # sweep every valid middle window and sum trio together before comparing to find global max
        max_total = -1
        answer = None
        for mid in range(k, len(window_sum) - k):
            left_idx = left_best_indices[mid - k]
            right_idx = right_best_indices[mid + k]
            total = window_sum[left_idx] + window_sum[mid] + window_sum[right_idx]
            if total > max_total:
                max_total = total
                answer = [left_idx, mid, right_idx]
        return answer
