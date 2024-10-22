"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

"""
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        #Edge Case
        if (x > (2**31 - 1)) or (x < (-2**31)):
            return 0
        
        negative_flag = False
        if x < 0:
            negative_flag = True
            mod_x = str(x * -1)
        else:
            mod_x = str(x)
            
        reversed_x = int(mod_x[::-1]) if not negative_flag else int(mod_x[::-1])*-1
        
        if (reversed_x > (2**31 - 1)) or (reversed_x < (-2**31)):
            return 0
        else:
            return reversed_x
        

class Solution:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x<0 else 1
        x_abs = abs(x)
        reversed_x = int(str(x_abs)[::-1]) * sign
        
        if -2**31 <= reversed_x <= 2**31 -1:
            return reversed_x
        else:
            return 0