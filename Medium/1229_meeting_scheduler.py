"""
1229. Meeting Scheduler

Given the availability time slots arrays `slots1` and `slots2` of two people and a meeting duration `duration`, return
the earliest time slot that works for both of them and is of duration `duration`.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from
`start` to `end`.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, 
for any two time slots `[start1, end1]` and `[start2, end2]` of the same person, either `start1 > end2`
or `start2 > end1`.
"""

"""
Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
"""

from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:

        # As a precaution - we pre-sort it O(nlogn)
        slots1.sort()
        slots2.sort()
        firstList_pointer, secondList_pointer = 0, 0

        while firstList_pointer < len(slots1) and secondList_pointer < len(slots2):
            firstList_start, firstList_end = slots1[firstList_pointer]
            secondList_start, secondList_end = slots2[secondList_pointer]

            interval_start = max(firstList_start, secondList_start)
            interval_end = min(firstList_end, secondList_end)

            if interval_end - interval_start >= duration:
                return [interval_start, interval_start + duration]

            if firstList_end < secondList_end:
                firstList_pointer += 1
            else:
                secondList_pointer += 1

        return []
