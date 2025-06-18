"""
3403. Find the Lexicographically Largest String From the Box I

You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds
in the game, where in each round:

- word is split into numFriends non-empty strings, such that no previous round has
had the exact same split.
- All the split words are put into a box.

Find the lexicographically largest string from the box after all the rounds are
finished.
"""

"""
Example 1:
Input: word = "dbca", numFriends = 2
Output: "dbc"

Explanation: 
All possible splits are:
"d" and "bca".
"db" and "ca".
"dbc" and "a".

Example 2:
Input: word = "gggg", numFriends = 4
Output: "g"

Explanation: 
The only possible split is: "g", "g", "g", and "g".
"""


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Edge Case
        if numFriends == 1:
            return word

        n = len(word)
        # logic: each friend gets at least 1 letter = numFriends
        # n - numFriends -> leftovers + 1 initial letter
        max_word_len = n - numFriends + 1

        def finds_lexicographically_greatest_suffix(s):
            start = 0
            next = 1
            offset = 0
            n = len(s)

            # comparing s[start + offset] and s[next + offset]
            while next + offset < n:
                if s[start + offset] == s[next + offset]:
                    # characters match, advance offset to compare further
                    offset += 1
                elif s[start + offset] > s[next + offset]:
                    next = next + offset + 1  # skip past the ruled-out block of the next
                    offset = 0
                else:
                    start = max(start + offset + 1, next)  # start is replaced
                    next = start + 1  # next begins 1 after start
                    offset = 0

            return s[start:]

        s = finds_lexicographically_greatest_suffix(word)
        return s[:max_word_len] if len(s) > max_word_len else s
