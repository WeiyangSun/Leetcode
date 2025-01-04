"""
65. Valid Number

Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", 
while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

1. An integer number followed by an optional exponent.
2. A decimal number followed by an optional exponent.

An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

1. Digits followed by a dot '.'.
2. Digits followed by a dot '.' followed by digits.
3. A dot '.' followed by digits.

An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.
"""

"""
Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false
"""
import re

class Solution:
    def isNumber(self, s: str) -> bool:

        """
        ^\s*             # Start of string, followed by any number of whitespaces
        [+-]?            # An optional '+' or '-'
        (                # Start of group for the main number
            \d+(\.\d*)?  ### Digits, optionally followed by a decimal point and maybe more digits
            |            ### OR
            \.\d+        ### A decimal point followed by one or more digits
        )                # End of group for the main number
        ([eE][+-]?\d+)?  # Optionally, an exponent part: e/E, optional sign, followed by digits
        \s*$             # Any number of whitespaces till the end of string
        """

        pattern_string = r'^\s*[+-]?(\d+(\.\d*)?|(\.\d+))([eE][+-]?\d+)?\s$'
        pattern = re.compile(pattern_string)

        return bool(pattern.match(s))

class Solution:
    def isNumber(self, s: str) -> bool:
        # Trim out Whitespaces
        s = s.strip()
        if not s:
            return False # Nothing left after trimming whitespaces

        # Flags
        seenDigit = False
        seenDecimal = False
        seenExponent = False

        n = len(s)
        ix = 0

        # Checking for positive or negative signs
        if ix < n and (s[ix] == '+' or s[ix] == '-'):
            ix += 1

        # Checking Digits and Decimals
        while ix < n:
            chr = s[ix]
            if chr.isdigit():
                seenDigit = True
                ix += 1
            elif chr == '.':
                if seenDecimal or seenExponent:
                    return False
                seenDecimal = True
                ix += 1
            else: # Not a digit or a decimal
                break

        # Checking Exponent
        if ix < n and (s[ix] == 'e' or s[ix] == 'E'):
            if seenDigit: # Did not see any digits before Exponent
                return False
            seenExponent = True
            ix += 1

            # Optional: Sign after Exponent
            if ix < n and (s[ix] == '+' or s[ix] == '-'):
                ix += 1

            if ix == n: # must see at least one digit after exponent
                return False

            # Flag to check for digits after Exponent
            seenDigitExponent = False
            while ix < n and s[ix].isdigit():
                seenDigitExponent = True
                ix += 1

            if not seenDigitExponent:
                return False

        if ix < n:
            return False

        return seenDigit