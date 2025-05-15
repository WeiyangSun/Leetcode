"""
1094. Car Pooling

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and
drive west).

You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengers_i, from_i, to_i]`
indicates that the i-th trip has `numPassengers_i` passengers and the locations to pick them up and drop them
off are `from_i` and `to_i` respectively. The locations are given as the number of kilometers due east
from the car's initial location.

Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or
`false` otherwise.
"""

"""
Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
"""

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        difference_log = [0] * 1001

        for passengers, start_ix, end_ix in trips:
            difference_log[start_ix] += passengers
            difference_log[end_ix] -= passengers

        current_capacity = 0
        for delta in difference_log:
            current_capacity += delta
            if current_capacity > capacity:
                return False
        return True


import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        current_capacity = 0
        on_board = []  # will capture (end_idx, passengers)

        for passengers, start_idx, end_idx in trips:
            while on_board and on_board[0][0] <= start_idx:
                leave_end, leave_passengers = heapq.heappop(on_board)
                current_capacity -= leave_passengers
            current_capacity += passengers
            if current_capacity > capacity:
                return False

            heapq.heappush(on_board, (end_idx, passengers))

        return True
