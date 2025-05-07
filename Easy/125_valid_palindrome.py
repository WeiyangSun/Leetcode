"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

"""
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false

Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true

Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

"""
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""


class SimpleSolution:
    def is_palindrome(self, s: str) -> bool:
        """
        # Example 1
        >>> sol = ConstantSolution()
        >>> sol.is_palindrome("A man, a plan, a canal: Panama")
        True

        # Example 2
        >>> sol.is_palindrome("race a car")
        False

        # Example 3
        >>> sol.is_palindrome("")
        True
        """
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]  # This is o(n) - depends on how long the string is


class ConstantSolution:
    def is_palindrome(self, s: str) -> bool:
        """
        # Example 1
        >>> sol = ConstantSolution()
        >>> sol.is_palindrome("A man, a plan, a canal: Panama")
        True

        # Example 2
        >>> sol.is_palindrome("race a car")
        False

        # Example 3
        >>> sol.is_palindrome("")
        True
        """
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                i, j = i + 1, j - 1
                continue

            # When encountering non-alphanumeric types, this line helps to skip it
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True

class ConstantSolution:
    def is_palindrome(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s)-1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            
            left_pointer += 1
            right_pointer -= 1

        return True