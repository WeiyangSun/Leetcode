"""
247. Strobogrammatic Number II

Given an integer n, return all the strobogrammatic numbers that are of length n.
You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees
(looked at upside down).
"""

"""
Example 1:
Input: n = 2
Output: ["11","69","88","96"]

Example 2:
Input: n = 1
Output: ["0","1","8"]
"""

from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        # Seed mirror-pairs that stay valid after 180-degree rotation
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

        def dfs(k, total):
            # Base Case
            if k == 0:
                return [""]  # one empty string = one valid core
            if k == 1:
                return ["0", "1", "8"]  # exception case where 0, 1 and 8 are self-mirroring

            # Recursive Step
            middles = dfs(k - 2, total) # because each recursive step fills two positions at once - one left one right
            result = []

            for mid in middles: # if k = 2; then here will be [""]
                for a, b in pairs:
                    # k == total is important because of the recursive nature
                    if k == total and a == "0": # prevents the last layer from choosing 0 as the leftmost digit
                        continue # skip this pair when it gives a leading 0
                    result.append(a + mid + b)  # growing by 1 layer

            return result

        return dfs(n, n)
