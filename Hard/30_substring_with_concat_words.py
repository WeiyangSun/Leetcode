"""
30. Substring with Concatenation of All Words

You are given a string `s` and an array of strings `words`. All the strings
of `words` are of the same length.

A concatenated string is a string that exactly contains all the strings
of any permutation of words concatenated.

- For example, if words = ["ab", "cd", "ef"], then "abcdef", "abefcd", 
"cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
"abcdbef" is not a concatenated string because it is not the concatenation
of any permutation of `words`.

Return an arrary of the starting indices of all the concatenated substrings
in `s`. You can return the answer in any order.
"""

"""
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]

Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
"""
from collections import Counter, defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_word_len = word_len * len(words)
        word_count = Counter(words)
        result = []
        
        for i in range(len(s) - total_word_len + 1):
            substring = s[i:i+total_word_len]
            seen = {}
            for j in range(0, total_word_len, word_len):
                word = substring[j:j+word_len]
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            else:
                result.append(i)

        return result

s = "barfoothefoobarman"
words = ["foo", "bar"]
sol = Solution()
print(sol.findSubstring(s, words))

from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def get_all_permutations(words):
            return [''.join(p) for p in permutations(words)]
        
        if not s or not words:
            return []
        
        permuted_words = get_all_permutations(words)
        result = []
        perm_set = set(permuted_words)
        perm_len = len(permuted_words[0])
        
        for i in range(len(s) - perm_len + 1):
            substring = s[i:i+perm_len]
            if substring in perm_set:
                result.append(i)
        return result

s = "barfoothefoobarman"
words = ["foo", "bar"]
sol = Solution()
print(sol.findSubstring(s, words))

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = Counter(words)
        num_words = len(words)
        result = []
        
        for i in range(word_len):
            left = i
            count = 0
            window_word_count = defaultdict(int)
            
            for j in range(i, len(s) - word_len+1, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    window_word_count[word] += 1
                    count += 1
                    
                    while window_word_count[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        window_word_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == num_words:
                        result.append(left)
                
                else:
                    window_word_count.clear()
                    count = 0
                    left = j + word_len
            
        return result
