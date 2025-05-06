"""
986. Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [start_i, end_i]
and secondList[j] = [start_j, end_j]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers `x` with `a <= x <= b`.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a
closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
"""

"""
Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        firstList_pointer, secondList_pointer = 0, 0

        while firstList_pointer < len(firstList) and secondList_pointer < len(secondList):
            firstList_start, firstList_end = firstList[firstList_pointer]
            secondList_start, secondList_end = secondList[secondList_pointer]

            interval_start = max(firstList_start, secondList_start)
            interval_end = min(firstList_end, secondList_end)

            if interval_start <= interval_end:
                result.append([interval_start, interval_end])

            if firstList_end < secondList_end:
                firstList_pointer += 1
            else:
                secondList_pointer += 1

        return result