"""
2566. Maximum Difference by Remapping a Digit

You are given an integer num. You know that Bob will sneakily remap
one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can
make by remapping exactly one digit in num.

Notes:

- When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences
    of d1 in num with d2.
- Bob can remap a digit to itself, in which case num does not change.
- Bob can remap different digits for obtaining minimum and maximum values
    respectively.
- The resulting number after remapping can contain leading zeroes.
"""

"""
Example 1:
Input: num = 11891
Output: 99009

Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.

Example 2:
Input: num = 90
Output: 99

Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9)
and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
"""

class Solution:
    def minMaxDifference(self, num: int) -> int:
        # convert input number to string
        num_str = str(num)
        max_diff = 0

        for each_number in set(num_str):
            max_candidate = int(num_str.replace(each_number, '9'))
            min_candidate = int(num_str.replace(each_number, '0'))
            diff = max_candidate - min_candidate
            max_diff = max(max_diff, diff)

        return max_diff

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        for d in num_str:
            if d != '9':
                max_str = num_str.replace(d, '9')
                break
            else:
                max_str = num_str

        for d in num_str:
            if d != '0':
                min_str = num_str.replace(d, '0')
                break
            else:
                min_str = num_str
        
        return int(max_str) - int(min_str)