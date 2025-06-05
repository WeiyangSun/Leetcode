"""
2131. Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any
order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome,
return 0.

A palindrome is a string that reads the same forward and backward.
"""

"""
Example 1:
Input: words = ["lc","cl","gg"]
Output: 6

Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8

Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2

Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
"""

from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # count frequency of each word
        word_count = Counter(words) # {"lc": 1, "cl": 1, "gg": 1}
        length = 0

        # iterate over all unique two-letter words
        for word in list(word_count.keys()):
            rev = word[::-1]
            if word == rev:
                # word is palindromic
                pairs = word_count[word] // 2
                length += pairs * 4 # each pair adds 4 to length
                word_count[word] -= pairs * 2 # remove used words from count
            else:
                # if word is different from its reverse
                if rev in word_count:
                    # find max pairs possible between word and its reverse
                    pairs = min(word_count[word], word_count[rev])
                    length += pairs * 4 # each pair adds 4 to length
                    word_count[word] -= pairs
                    word_count[rev] -= pairs

        # after all pairs, check if any palindromic word is left for the center
        for word in word_count:
            if word[0] == word[1] and word_count[word] > 0:
                length += 2
                break

        return length