"""
3362. Zero Array Transformation III

You are given an integer array nums of length n and a 2D array queries where queries[i] = [l_i, r_i].

Each queries[i] represents the following action on nums:

- Decrement the value at each index in the range [l_i, r_i] in nums by at most 1.
- The amount by which the value is decremented can be chosen independently for each index.

A zero array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted
to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.
"""

"""
Example 1:
Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
Output: 1

Explanation:
After removing queries[2], nums can still be converted to a zero array.
Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.

Example 2:
Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]
Output: 2

Explanation:
We can remove queries[2] and queries[3].

Example 3:
Input: nums = [1,2,3,4], queries = [[0,3]]
Output: -1

Explanation:
nums cannot be converted to a zero array even after using all the queries.
"""

from typing import List
import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Preprocessing
        # sort by start-index so we can sweep left -> right
        queries.sort(key=lambda p: p[0])

        available_max = []  # max-heap (store - r) = blankets we could take
        running_min = []  # min-heap (store r) = blankets we already took
        qi = 0  # pointer to next query that becomes available

        n, m = len(nums), len(queries)

        # Sweep Array
        for i in range(n):
            # Add every query whose l <= i to the available heap
            while qi < m and queries[qi][0] <= i:
                heapq.heappush(available_max, -queries[qi][1])
                qi += 1

            # Drop from running_min every blanket that no longer covers i
            while running_min and running_min[0] < i:
                heapq.heappop(running_min)

            # Ensure we have at least nums[i] blankets on i
            while nums[i] > len(running_min):
                if not available_max:  # nothing left that can reach i = impossible
                    return -1
                furthest_r = -heapq.heappop(available_max)  # longest blanket
                if furthest_r < i:  # still can't reach i = impossible
                    return -1
                heapq.heappush(running_min, furthest_r)

        return len(available_max) + (m - qi)
