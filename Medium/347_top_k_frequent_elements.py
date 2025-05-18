"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the
answer in any order.
"""

"""
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency[num].get(num, 0) + 1

        min_heap = []
        for num, count in frequency.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for _, num in min_heap]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)

        min_heap = []
        for num, count in frequency_counter.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for _, num in min_heap]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)

        # buckets contain - frequency : list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in frequency_counter.items():
            buckets[count].append(num)

        result = []
        for f in range(len(nums), 0, -1):
            for num in buckets[f]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
