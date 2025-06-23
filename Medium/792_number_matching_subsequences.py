"""
792. Number of Matching Subsequences

Given a string s and an array of strings words, return the number of
words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original
string with some characters (can be none) deleted without changing the
relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
"""

"""
Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3

Explanation: There are three strings in words that are a subsequence
of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
"""

from typing import List
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        character_map = defaultdict(list) # dictionary to hold list of (word, index_pointer) pair for each character
        # for every word in the list of words, we will only pick the first letter first
        # only when the first letter matches, then we will proceed mapping the second character later
        # this will serve as an individual word pointer. only when pointer == len(word) then it is a valid subsequence
        for word in words:
            character_map[word[0]].append((word, 0))

        subsequence_count = 0
        for char in s:
            cur_word_list = character_map[char] # get current list of (word, index) matching this character
            # reset list for this character
            character_map[char] = []
            # process all words in cur_word_list
            for word, index in cur_word_list:
                index += 1 # moving pointer to next letter in word
                if index == len(word):
                    subsequence_count += 1
                else:
                    character_map[word[index]].append((word, index))

        return subsequence_count