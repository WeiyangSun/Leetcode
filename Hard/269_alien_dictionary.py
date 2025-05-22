"""
269. Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order of the letters
is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that
the strings in the words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any
order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically
increasing order by the new language's rules. If there are multiple solutions, return any of them.
"""

"""
Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""

Explanation: The order is invalid, so return "".
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 1. Build graph
        # adj_letter: letter -> letter that must come after it
        adj_letter = defaultdict(set)
        # word_arrow_frequency:  letter -> number of incoming edges (prerequisites)
        word_arrow_frequency = {char: 0 for word in words for char in word}

        # Comparing neighboring words to discover precedence rules
        for curr_word, next_word in zip(words, words[1:]):  # look at every adjacent pair
            for curr_word_char, next_word_char in zip(
                curr_word, next_word
            ):  # scan both words side by side
                if curr_word_char != next_word_char:  # first difference found
                    if next_word_char not in adj_letter[curr_word_char]:  # avoid duplicate records
                        adj_letter[curr_word_char].add(
                            next_word_char
                        )  # shows relationship from c1 -> c2
                        word_arrow_frequency[next_word_char] += 1  # c2 gains a prerequisite
                    break
            else:
                if len(curr_word) > len(next_word):
                    return ""

        # 2. Topological sort
        # queue starts with letters that have no prerequisites
        queue = deque([char for char, pre in word_arrow_frequency.items() if pre == 0])
        alphabet_order = []
        while queue:
            char = queue.popleft()
            alphabet_order.append(char)
            for nxt in adj_letter[char]:
                word_arrow_frequency[nxt] -= 1
                if word_arrow_frequency[nxt] == 0:
                    queue.append(nxt)

        return "".join(alphabet_order) if len(alphabet_order) == len(word_arrow_frequency) else ""
