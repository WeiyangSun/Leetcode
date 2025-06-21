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
        window = [0] * (n - k + 1)  # rolling sum
        cur_window = sum(nums[:k])
        window[0] = cur_window
        for i in range(1, n - k + 1):
            cur_window += nums[i + k - 1] - nums[i - 1]
            window[i] = cur_window

        # left-to-right: where is the best window that we already passed
        left_best = [0] * len(window)
        best = 0
        for i in range(len(window)):
            if window[i] > window[best]:
                best = i
            left_best[i] = best

        # right-to-left: where is the best window that we will still meet
        right_best = [0] * len(window)
        best = len(window) - 1
        for i in range(len(window) - 1, -1, -1):
            if window[i] >= window[best]:
                best = i
            right_best[i] = best

        # sweep every valid middle window and glue trio together
        max_total = -1
        answer = None
        for mid in range(k, len(window) - k):
            left = left_best[mid - k]
            right = right_best[mid + k]
            total = window[left] + window[mid] + window[right]
            if total > max_total:
                max_total = total
                answer = [left, mid, right]
        return answer
