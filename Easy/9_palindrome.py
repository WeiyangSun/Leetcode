"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
"""

"""
Example 1:
Input: x = 121
Output: true

Explanation: 121 reads as 121 from left to right and from right to left

Example 2:
Input: x = -121
Output: false

Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false

Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        pointer_A, pointer_B = 0, len(x)-1

        while pointer_A <= len(x)//2:
            if x[pointer_A] == x[pointer_B]:
                pointer_A += 1
                pointer_B -= 1
            else:
                return False

        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_num = x
        reversed_num = 0

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num*10 + digit
            x = x // 10

        return original_num == reversed_num

sol = Solution()
print(sol.isPalindrome(-121))