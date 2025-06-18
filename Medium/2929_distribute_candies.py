"""
2929. Distribute Candies Among Children II

You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such
that no child gets more than limit candies.
"""

"""
Example 1:
Input: n = 5, limit = 2
Output: 3

Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 
2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

Example 2:
Input: n = 3, limit = 3
Output: 10

Explanation: There are 10 ways to distribute 3 candies such that no child gets more than
3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0),
(2, 0, 1), (2, 1, 0) and (3, 0, 0).
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Base Case
        if (
            n > 3 * limit
        ):  # total candies exceed the max, no valid way that a child can remain under limit
            return 0

        def combinations(m):
            if m < 0:
                return 0
            # logic: stars-bars - we have (n+(k-1)) spots to choose (k-1) from
            # example 7C2 can be reduced to 7!/2!(7-2)! = 7*6*5!/2!(5!) = (7*6)/2!
            return (m + 2) * (m + 1) // 2

        k = limit + 1  # threshold beyond a child is over-limit

        # Inclusion–exclusion:
        # 1) ways(n): all distributions without limit
        # 2) 3*ways(n-k): subtract when at least any single box is over limit
        # 3) 3*ways(n-2*k): add back when double box both over limit - this is because it was already counted in the one box over limit
        # 4) ways(n-3*k): subtract if all trip box exceed (always zero here unless n very large)
        return (
            combinations(n)
            - 3 * combinations(n - k)
            + 3 * combinations(n - 2 * k)
            - combinations(n - 3 * k)
        )
