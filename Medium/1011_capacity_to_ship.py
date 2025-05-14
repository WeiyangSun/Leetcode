"""
1011. Capacity to Ship Packages within D Days

A conveyor belt has packages that must be shipped from one port to another within X days.

The i-th package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt
(in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within
X days.
"""

"""
Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15

Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6

Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3

Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low_guess, high_guess = max(weights), sum(weights)

        while low_guess < high_guess:
            mid_guess = (low_guess + high_guess) // 2

            days_count = 1
            total_load = 0
            for weight in weights:
                if total_load + weight > mid_guess:
                    days_count += 1
                    total_load = 0
                total_load += weight

            if days_count <= days:
                high_guess = mid_guess
            else:
                low_guess = mid_guess + 1

        return low_guess


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def weight_days_calculation(guess):
            days_needed = 1
            running_total = 0

            for weight in weights:
                if running_total + weight > guess:
                    days_needed += 1
                    running_total = 0
                running_total += weight

            return days_needed

        low_guess, high_guess = max(weights), sum(weights)

        while low_guess < high_guess:
            mid_guess = (high_guess + low_guess) // 2

            if weight_days_calculation(mid_guess) <= days:
                high_guess = mid_guess
            else:
                low_guess = mid_guess + 1

        return low_guess


class Solution:
    @staticmethod
    def _days_needed(weights: List[int], capacity: int) -> int:
        days_needed, running_total = 1, 0
        for weight in weights:
            if running_total + weight > capacity:
                days_needed += 1
                running_total = 0
            running_total += weight
        return days_needed

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low_guess, high_guess = max(weights), sum(weights)
        while low_guess < high_guess:
            mid_guess = (low_guess + high_guess) // 2
            if Solution._days_needed(weights, mid_guess) > D:
                low_guess = mid_guess + 1
            else:
                high_guess = mid_guess
        return low_guess 