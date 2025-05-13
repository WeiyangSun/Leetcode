"""
3527. Find the Most Common Response

You are given a 2D string array responses where each responses[i] is an array of strings representing survey
responses from the i-th day.

Return the most common response across all days after removing duplicate responses within each responses[i].
If there is a tie, return the lexicographically smallest response.
"""

"""
Example 1:
Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
Output: "good"

Explanation:
After removing duplicates within each list, responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]].
"good" appears 3 times, "ok" appears 2 times, and "bad" appears 2 times.
Return "good" because it has the highest frequency.

Example 2:
Input: responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
Output: "bad"

Explanation:
After removing duplicates within each list we have responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]].
"bad", "good", and "ok" each occur 2 times.
The output is "bad" because it is the lexicographically smallest amongst the words with the highest frequency.
"""

from typing import List
from collections import Counter


class Solution:
    def findCommonResponse(self, response: List[List[str]]) -> str:

        freq = Counter()

        for each_day in response:
            for ans in set(each_day):
                freq[ans] += 1

        max_count = max(freq.values())
        return min(ans for ans, cnt in freq.items() if cnt == max_count)


class Solution:
    def findCommonResponse(self, response: List[List[str]]) -> str:

        freq = Counter(word for r in response for word in set(r))
        max_freq = max(freq.values())
        return min(word for word, cnt in freq.items() if cnt == max_freq)
