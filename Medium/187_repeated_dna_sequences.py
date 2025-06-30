"""
187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as
'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long
sequences (substrings) that occur more than once in a DNA molecule. You may return
the answer in any order.
"""

"""
Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # set to store all 10-letter sequences seen so far
        seen = set()
        # set to store sequences seen more than once
        repeated = set()

        for i in range(len(s) - 9):
            seq = s[i : i + 10]  # get 10 letter substring
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        return list(repeated)
