"""
126. Word Ladder II

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a
sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

1. Every adjacent pair of words differs by a single letter.
2. Every `s1` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
3. `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return all the shortest
transformation sequences from `beginWord` to `endWord`, or an empty list if no such sequence extsts.
Each sequence should be returned as a list of the words `[beginWord, s1, s2, ... sk]`.
"""

"""
Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []

Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation
sequence.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Build tree with BFS
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in wordSet:
                            for path in layer[word]:
                                new_layer[new_word].append(path + [new_word])

            wordSet -= set(new_layer.keys())
            layer = new_layer

        return []