"""
564. Find the Closest Palindrome

Given a string n representing an integer, return the closest integer (not including itself), which is a
palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.
"""

"""
Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"

Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length_n = len(n)
        num_n = int(n)
        candidates = set()

        # Add edge Palindromes
        candidates.add(str(10 ** (length_n - 1) - 1))
        candidates.add(str(10**length_n + 1))

        # Generate palindromes by mirroring
        prefix_n = int(n[: (length_n + 1) // 2])
        prefix_array = [-1, 0, 1]

        for variation in prefix_array:
            new_prefix = str(prefix_n + variation)
            if length_n % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)

        closest_palindrome = None
        min_difference = float("inf")
        for candidate in candidates:
            if candidate == n or candidate.startswith("-"):
                continue
            actual_difference = abs(int(candidate) - num_n)
            # Tiebreaker Condition = if difference is the same, pick smaller number
            if (actual_difference < min_difference) or (
                actual_difference == min_difference and int(candidate) < int(closest_palindrome)
            ):
                min_difference = actual_difference
                closest_palindrome = candidate

        return closest_palindrome
