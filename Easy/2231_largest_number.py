"""
2231. Largest Number After Digit Swaps by Parity

You are given a positive integer num. You may swap any two digits of
num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.
"""

"""
Example 1:
Input: num = 1234
Output: 3412

Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

Example 2:
Input: num = 65875
Output: 87655

Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
"""

"""
Constraints:
1 <= num <= 109
"""

class Solution:
    def largestInteger(self, num: int) -> int:
        n = len(str(num))
        num_list = [int(i) for i in str(num)]
        odd_list, even_list = [], []

        for num in num_list:
            if num % 2 == 0: 
                even_list.append(num)
            odd_list.append(num)
        
        odd_list.sort()
        even_list.sort()

        result = 0
        for i in range(n):
            if num_list[i] % 2 == 0:
                result = result*10 + even_list.pop() #multiplied by 10 to move 10s, 100s etc.
            result = result*10 + odd_list.pop()

        return result