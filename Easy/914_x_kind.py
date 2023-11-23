"""
914. X of a Kind in a Deck of Cards

You are given an integer array deck where deck[i] represents
the number written on the ith card.

Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.
"""

from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: list(int)) -> bool:

        c = Counter(deck)
        global_min = min(c.values())

        if global_min < 2:
            return False
        for i in range(global_min + 1, 1, -1):
            res = all(v%i == 0 for v in c.values())
            if res:
                return True
        
        return False
    
import math
import functools
class Solution:
    def hasGroupsSizeX(self, deck: list(int)) -> bool:

        c = Counter(deck)
        return functools.reduce(math.gcd, c.values()) != 1