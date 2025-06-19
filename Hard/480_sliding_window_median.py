"""
480. Sliding Window Median

The median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle values.

- For example, if arr = [2,3,4], the median is 3.
- For example, if arr = [1,2,3,4], the median is (2+3) / 2 = 2.5.

You are given an integer array nums and an integer k. There is a sliding window
of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves
right by one position.

Return the median array for each window in the original array. Answers within
10**-5 of the actual value will be accepted.
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
        # max_heap catches the smaller half of the numbers - quickly get largest of the small half
        # min_heap catches the larger half of the numbers - quickly get smallest of the large half
        smaller_half, larger_half = [], [] 
        delayed = defaultdict(int) # counts of elements to lazily remove
        small_size = large_size = 0

        def prune(heap):
            # removes the top of a heap if it is marked for deletion in delayed
            # keeps popping until top is a valid element
            while heap:
                # determine the real value at heap top
                num = -heap[0] if heap is smaller_half else heap[0]
                if delayed[num] > 0:
                    # decrement delayed count and pop it from heap
                    delayed[num] -= 1
                    if delayed[num] == 0:
                        del delayed[num]
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal small_size, large_size
            # Case 1: smaller_half is bigger than larger_half
            if small_size > large_size:
                val = -heapq.heappop(smaller_half)
                small_size -= 1
                heapq.heappush(larger_half, val)
                large_size += 1
                prune(smaller_half)

            # Case 2: larger_half is bigger than smaller_half
            elif large_size > small_size:
                val = heapq.heappop(larger_half)
                large_size -= 1
                heapq.heappush(smaller_half, -val)
                small_size += 1
                prune(larger_half)

        def insert_into(num):
            nonlocal small_size, large_size
            # value is smaller than the largest value in the smaller_half
            if not smaller_half or num <= -smaller_half[0]:
                # push into smaller half
                heapq.heappush(smaller_half, -num)
                small_size += 1
            else:
                heapq.heappush(larger_half, num)
                large_size += 1
            rebalance()

        def erase(num):
            nonlocal small_size, large_size
            delayed[num] += 1 # marking for lazy deletion
            # adjust active sizes:
            if num <= -smaller_half[0]:
                small_size -= 1
                # if the num is at the top, prune immediately
                if num == -smaller_half[0]:
                    prune(smaller_half)
            else:
                large_size -= 1
                if larger_half and num == larger_half[0]:
                    prune(larger_half)
            rebalance()

        def get_current_median():
            if k % 2:
                return float(-smaller_half[0])
            return (-smaller_half[0] + larger_half[0]) / 2.0

        # initializing for first sliding window
        for num in nums[:k]:
            insert_into(num)
        result = [get_current_median()]
        # for remaining sliding windows
        for i in range(k, len(nums)):
            insert_into(nums[i])
            erase(nums[i-k])
            result.append(get_current_median())

        return result