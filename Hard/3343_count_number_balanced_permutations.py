"""
3343. Count Number of Balanced Permutations

You are given a string num. A string of digits is called balanced if the sum of the digits
at even indices is equal to the sum of the digits at odd indices.

Return the number of distinct permutations of num that are balanced.

Since the answer may be very large, return it modulo 10**9 + 7.

A permutation is a rearrangement of all the characters of a string.
"""

"""
Example 1:
Input: num = "123"
Output: 2

Explanation:

The distinct permutations of num are "123", "132", "213", "231", "312" and "321".
Among them, "132" and "231" are balanced. Thus, the answer is 2.

Example 2:
Input: num = "112"
Output: 1

Explanation:

The distinct permutations of num are "112", "121", and "211".
Only "121" is balanced. Thus, the answer is 1.

Example 3:
Input: num = "12345"
Output: 0

Explanation:

None of the permutations of num are balanced, so the answer is 0.
"""

from functools import lru_cache
from math import comb, factorial


class Solution:
    def countBalancedPermutations(self, num: str) -> int:

        MOD = 10**9 + 7
        count = [0] * 10  # used to capture the frequency of each digits
        total_sum = 0
        for char in num:
            d = int(char)
            count[d] += 1
            total_sum += d

        if total_sum % 2 == 1:  # if you have one less odd digit than even
            return 0

        half_total = total_sum // 2
        n = len(num)
        odd_slots = n // 2
        even_slots = (n + 1) // 2  # gives 1 extra when n is odd

        @lru_cache(
            maxsize=None
        )  # lru_cache prevents recomputing if we have previously entered that state
        def dfs(digit: int, need: int, odd_slot: int, even_slot: int) -> int:
            # If we finished all digits and everything matches perfectly, that’s one good permutation; otherwise none.
            if digit == 10:
                return 1 if need == odd_slot == even_slot == 0 else 0
            if odd_slot == 0 and need:  # no more odd slots but still have weights to place
                return 0

            ways = 0
            digit_frequency = count[digit]
            # try putting l copies into odd bucket, rest into even bucket
            for initial_frequency in range(min(digit_frequency, odd_slot) + 1):
                remaining_freq = (
                    digit_frequency - initial_frequency
                )  # Whatever doesn’t go into the odd bucket, goes into the even bucket
                if (
                    remaining_freq > even_slot
                ):  # Skip this split if the even bucket hasn’t enough holes
                    continue
                weight = initial_frequency * digit
                if weight > need:  # if weight would make the odd bucket heavier than allowed
                    continue
                ways += (
                    comb(
                        odd_slot, initial_frequency
                    )  # how many different ways we can drop the same number into different parts of the odd bucket
                    * comb(
                        even_slot, remaining_freq
                    )  # how many different ways we can drop the remaining number into different parts of the even bucket
                    * dfs(
                        digit + 1,
                        need - weight,
                        odd_slot - initial_frequency,
                        even_slot - remaining_freq,
                    )  # place next digit into the remaining slots available
                )
                # using a modulus—keeping numbers tiny and runtime quick
                ways %= MOD  # Capping answer to Mod

            return ways

        # counts every way the digits can be dropped into slots
        initial_ways = dfs(0, half_total, odd_slots, even_slots)

        duplication_denominator = 1
        # This will only increment if you have digits with more than 1 frequency
        for c in count:  # using a modulus—keeping numbers tiny and runtime quick
            duplication_denominator = duplication_denominator * factorial(c) % MOD

        # Fermat Inverse - need this because duplication_denominator has been MOD and initial_ways has been MOD
        inverse_duplication = pow(
            duplication_denominator, MOD - 2, MOD
        )  # inverse_duplication is the number that makes duplication_denominator * inverse_duplication = 1
        # once you’ve stepped into modular arithmetic, “divide” is performed by multiplying with the modular inverse, not by the / operator.
        return initial_ways * inverse_duplication % MOD
