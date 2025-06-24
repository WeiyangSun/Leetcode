"""
408. Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty
substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not
limited to):

- "s10n" ("s ubstitutio n")
- "sub4u4" ("sub stit u tion")
- "12" ("substitution")
- "su3i1u2on" ("su bst i t u ti on")
- "substitution" (no substrings replaced)

The following are not valid abbreviations:

- "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
- "s010n" (has leading zeros)
- "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches 
the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
"""

"""
Example 1:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true

Explanation: The word "internationalization" can be abbreviated as "i12iz4n"
("i nternational iz atio n").

Example 2:
Input: word = "apple", abbr = "a2e"
Output: false

Explanation: The word "apple" cannot be abbreviated as "a2e".
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_pointer = 0
        abbr_pointer = 0

        while word_pointer < len(word) and abbr_pointer < len(abbr):
            if abbr_pointer.isdigit():
                # if the current character in abbr is a digit that starts with '0'
                if abbr[abbr_pointer] == "0":
                    return False

                # mechanism to convert multiple digit in string format to numerical
                num = 0
                while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                    num = num * 10 + int(abbr[abbr_pointer])
                    abbr_pointer += 1

                # skip numerical characters in word
                word_pointer += num

            else:
                if word[word_pointer] != abbr[abbr_pointer]:
                    return False
                word_pointer += 1
                abbr_pointer += 1

        return word_pointer == len(word) and abbr_pointer == len(abbr)
