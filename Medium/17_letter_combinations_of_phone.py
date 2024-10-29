"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
number could present. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does
not map to any letters.

2: "abc"
3: "def"
4: "ghi"
5: "jkl"
6: "mno"
7: "pqrs"
8: "tuv"
9: "wxyz"
"""

"""
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        number_to_letters_map = {"2": "abc",
                                "3": "def",
                                "4": "ghi",
                                "5": "jkl",
                                "6": "mno",
                                "7": "pqrs",
                                "8": "tuv",
                                "9": "wxyz"
                                }

        result = []
        combination = []

        def backtrack(index):
            if index == len(digits):
                result.append("".join(combination))
                return

            current_digit = digits[index]
            letters = number_to_letters_map.get(current_digit, "")

            for letter in letters:
                combination.append(letter)
                backtrack(index+1)
                combination.pop()

        backtrack(0)
        return result

sol = Solution()
print(sol.letterCombinations(digits="23"))