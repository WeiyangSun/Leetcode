"""
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the i-th
station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from
the ith station to its next (i + 1)th station. You begin the journey with an empty tank
at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you
can travel around the circuit once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique.
"""

"""
Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0 # net fuel over the entire journey - is the trip physically possible at all?
        current_tank = 0 # net fuel while testing the current start gas station - have we run dry so far starting from our current point?
        start_station = 0 # index of the current candidate starting position

        for i in range(len(gas)):
            diff = gas[i] - cost[i] # calculates delta leaving for the next station
            total_tank += diff
            current_tank += diff

            # if current tank dips below zero, then journey fails
            if current_tank < 0:
                start_station = i+1 # next station is the new valid starting point
                current_tank = 0 # resets fuel tank for current journey
        
        return start_station if total_tank >= 0 else -1