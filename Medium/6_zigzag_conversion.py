"""
6. Zigzag Conversion

The string 'PAYPALISHIRING' is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);
"""

"""
Example 1:
Input: s = 'PAYPALISHIRING', numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        #Edge Case
        if numRows == 1 or numRows >= len(s):
            return s
        
        going_down = False
        rows = ['']*numRows
        current_row = 0
        
        for each_char in s:
            rows[current_row] += each_char
            
            # Flips at the top and bottom of a sequence
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            current_row += 1 if going_down else -1
            
        return ''.join(rows)
            
                
sol = Solution()
print(sol.convert(s = "PAYPALISHIRING", numRows=3))