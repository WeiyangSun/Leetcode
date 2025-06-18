"""
3170. Lexicographically Minimum String After Removing Stars

You are given a string s. It may contain any number of '*' characters.
Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left.
If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*'
characters.
"""

"""
Example 1:
Input: s = "aaba*"
Output: "aab"

Explanation:
We should delete one of the 'a' characters with '*'. If we choose s[3],
s becomes the lexicographically smallest.

Example 2:
Input: s = "abc"
Output: "abc"

Explanation:
There is no '*' in the string.
"""


class Solution:
    def clearStars(self, s: str) -> str:
        result = list(s)  # convert string to list -> "abc" to ["a", "b", "c"]
        buckets = [[] for _ in range(26)]  # one bucket per letter 'a' to 'z'

        for idx, char in enumerate(s):
            if char == "*":
                result[idx] = ""  # remove * immediately
                # now to find the smallest non-* letter
                for j in range(26):
                    if buckets[j]:
                        removal_idx = buckets[
                            j
                        ].pop()  # remove the latest occurrence to get lexicographically smallest
                        result[removal_idx] = ""
                        break
            else:
                buckets[ord(char) - ord("a")].append(idx)

        return "".join(result)
