"""
127. Word Ladder

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a
sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk` == endWord

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in
the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.
"""

"""
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0

Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        L = len(beginWord) # Assuming all words are the same length
        graph = defaultdict(list)

        # Pre-build wildcard buckets
        for word in wordSet:
            for i in range(L):
                bucket = word[:i] + '*' + word[i+1:]
                graph[bucket].append(word)

        # BFS
        queue = deque([(beginWord, 1)]) # (current_word, distance)
        visited = {beginWord}

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist

            for i in range(L):
                bucket = word[:i] + '*' + word[i+1:]
                for neighbor in graph[bucket]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append((neighbor, dist+1))
                graph[bucket].clear()

        return 0