"""
253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum
number of conference rooms required.
"""

"""
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        start_times = sorted(interval[0] for interval in intervals)
        end_times = sorted(interval[1] for interval in intervals)

        start_pointer, end_pointer = 0, 0
        used_rooms, max_rooms = 0, 0

        while start_pointer < len(intervals):
            # if the next meeting starts after or at the earliest ending meeting
            if start_times[start_pointer] >= end_times[end_pointer]:
                # release room
                used_rooms -= 1
                end_pointer += 1
            # allocate a room for current meeting
            used_rooms += 1
            max_rooms = max(max_rooms, used_rooms)
            # move to next meeting start time
            start_pointer += 1

        return max_rooms
