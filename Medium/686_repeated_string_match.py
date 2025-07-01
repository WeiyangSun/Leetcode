"""
686. Repeated String Match

Given two strings a and b, return the minimum number of times you should repeat
string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be
a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated
2 times is "abcabc".
"""

"""
Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3

Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b
is a substring of it.

Example 2:
Input: a = "a", b = "aa"
Output: 2
"""


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a  # start with one copy of a
        count = 1

        # repeat until repeated string length is at least as long as b
        while len(repeated) < len(b):
            repeated += a
            count += 1

        # check if b is now a substring
        if b in repeated:
            return count

        # check one more repetition in case b spans boundary
        repeated += a
        if b in repeated:
            return count + 1

        return -1
