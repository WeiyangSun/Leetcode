"""
480. Sliding Window Median

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle values.

- For example, if arr = [2,3,4], the median is 3.
- For example, if arr = [1,2,3,4], the median is (2+3) / 2 = 2.5.

You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the median array for each window in the original array. Answers within 10**-5 of the actual value will be accepted.
"""

"""
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]

Explanation: 

Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

Example 2:
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
"""

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap, min_heap = [], []
        delayed = defaultdict(int)
        size_max = size_min = 0
        medians = []

        def prune(heap):
            while heap and delayed[heap[0][1]]:
                delayed[heap[0][1]] -= 1
                heapq.heappop(heap)

        def rebalance():
            nonlocal size_max, size_min
            if size_max > size_min +1:
                val, idx = heapq.heappop(max_heap)
                heapq.heappush(min_heap, (-val, idx))
                size_max -= 1
                size_min += 1
            elif size_max < size_min:
                val, idx = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-val, idx))
                size_min -= 1
                size_max += 1

        def get_current_median():
            if k % 2:
                return float(-max_heap[0][0])
            return ((-max_heap[0][0] + min_heap[0][0]) / 2)

        # initialize the heaps
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        size_max = k
        for _ in range(k // 2):
            val, idx = heapq.heappop(max_heap)
            heapq.heappush(min_heap, (-val, idx))
            size_max -= 1
            size_min += 1
        
        rebalance()
        prune(max_heap)
        prune(min_heap)
        medians.append(get_current_median())

        # slide the window
        for i in range(k, len(nums) + 1):
            left = i - k
            delayed[left] += 1
            if nums[left] <= -max_heap[0][0]:
                size_max -= 1
                if nums[left] == -max_heap[0][0]:
                    prune(max_heap)
            else:
                size_min -= 1
                if nums[left] == min_heap[0][0]:
                    prune(min_heap)

            if nums[i] <= -max_heap[0][0]:
                heapq.heappush(max_heap, (-nums[i], i))
                size_max += 1
            else:
                heapq.heappush(min_heap, (nums[i], i))
                size_min += 1

            rebalance()
            prune(max_heap)
            prune(min_heap)
            medians.append(get_current_median())

        return medians