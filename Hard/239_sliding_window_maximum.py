"""
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.
"""

"""
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()  # holds indices of potential max elements

        for ix, val in enumerate(nums):
            # remove indices from front if they are out of the current window
            if window and window[0] <= ix - k:  # oldest index is too far left
                window.popleft()  # pop from the front

            # remove indices where corresponding values are less than current num
            # any index whose value is <= current_value can never be a max again, so remove from the back
            while window and nums[window[-1]] < val:
                window.pop()

            # add current element index to the back
            window.append(ix)

            # append to result when we have our first full window
            if ix >= k - 1:  # window now covers k elements
                result.append(nums[window[0]])  # front of window is the maximum

        return result
