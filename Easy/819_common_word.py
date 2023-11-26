"""
819. Most Common Word

Given a string paragraph and a string array of the banned
words banned, return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned,
and that the answer is unique.

The words in paragraph are case-insensitive and the answer
should be returned in lowercase.
"""

"""
Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it
was hit.", banned = ["hit"]
Output: "ball"

Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most
frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because
it is banned.

Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
"""

"""
Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the
symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
"""
import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph:str, banned:list(str)) -> str:
        cleaned_paragraph = re.sub("[!?',;.]", " ", paragraph)
        cleaned_paragraph_list = cleaned_paragraph.lower().split(' ')
        cleaned_paragraph_list = [x.strip() for x in cleaned_paragraph_list if len(x) != 0]
        cleaned_paragraph_list = [x for x in cleaned_paragraph_list if x not in banned]

        c = Counter(cleaned_paragraph_list)

        return [key for key, val in c.items() if val == max(c.values())][0]

class Solution:
    def mostCommonWord(self, paragraph:str, banned:list(str)) -> str:
        cleaned_paragraph_list = re.sub("[!?',;.]", " ", paragraph).lower().split(' ')
        cleaned_paragraph_list = [x.strip() for x in cleaned_paragraph_list if len(x) != 0]
        cleaned_paragraph_list = [x for x in cleaned_paragraph_list if x not in banned]

        c = Counter(cleaned_paragraph_list)

        return c.most_common(1)[0][0]

class Solution:
    def mostCommonWord(self, paragraph:str, banned:list(str)) -> str:
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        c = Counter(w for w in words if w not in ban)

        return c.most_common(1)[0][0]