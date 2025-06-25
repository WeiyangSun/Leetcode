"""
824. Goat Latin

You are given a string sentence that consist of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language
similar to Pig Latin.) The rules of Goat Latin are as follows:

- If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the
    end of the word.
        - For example, the word "apple" becomes "applema".
- If a word begins with a consonant (i.e., not a vowel), remove the first letter
    and append it to the end, then add "ma".
        - For example, the word "goat" becomes "oatgma".
- Add one letter 'a' to the end of each word per its word index in the sentence,
    starting with 1.
        - For example, the first word gets "a" added to the end, the second word 
        gets "aa" added to the end, and so on.

Return the final sentence representing the conversion from sentence to Goat Latin.
"""

"""
Example 1:
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa
hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        word_list = sentence.split()
        vowel_set = set("aeiouAEIOU")
        result = []

        for idx, word in enumerate(word_list):
            # check if first letter is a vowel
            if word[0] in vowel_set:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word += "a" * (idx + 1)
            result.append(goat_word)

        return " ".join(result)
