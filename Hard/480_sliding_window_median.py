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
        delayed = defaultdict(int) # count of elements marked for lazy deletion
        result = [] # used to store median

        def _prune(heap):
            # remove elements from top that are marked for deletion
            while heap and delayed[heap[0]] > 0:
                delayed[heap[0]] -= 1
                heapq.heappop(heap)

        def _rebalance():
            # balancing the 2 heaps
            if len(max_heap) > len(min_heap) + 1:
                val, idx = heapq.heappop(max_heap)
                heapq.heappush(min_heap, (-val, idx))
                _prune(max_heap)
            elif len(max_heap) < len(min_heap):
                val, idx = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-val, idx))
                _prune(min_heap)

        def _get_median():
            #if window size is odd, take from max_heap
            if k % 2:
                return float(-max_heap[0][0])
            else:
                return (-max_heap[0][0] + min_heap[0][0]) / 2

        # initialize heaps with first k elements
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        for _ in range(k // 2):
            val, idx = heapq.heappop(max_heap)
            heapq.heappush(min_heap, (-val, idx))
        result.append(_get_median())

        for i in range(k, len(nums)):
            outgoing_num, incoming_num = nums[i-k], nums[i]
            outgoing_idx, incoming_idx = i-k, i

            if outgoing_num <= -max_heap[0][0]: # determining whether max_heap
                # mark tuple for lazy deletion
                delayed[(-outgoing_num, outgoing_idx)] += 1
            else:
                delayed[(outgoing_num, outgoing_idx)] += 1

            if incoming_num <= -max_heap[0][0]:
                heapq.heappush(max_heap, (-incoming_num, incoming_idx))
            else:
                heapq.heappush(min_heap, (incoming_num, incoming_idx))

            # prune both heaps
            _prune(max_heap)
            _prune(min_heap)
            _rebalance()
            result.append(_get_median())
    
        return result