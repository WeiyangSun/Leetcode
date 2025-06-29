"""
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order,
and an integer k.

Return the kth positive integer that is missing from this array.
"""

"""
Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9

Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...].
The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6

Explanation: The missing positive integers are [5,6,7,...].
The 2nd missing positive integer is 6.
"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left_pointer, right_pointer = 0, len(arr) - 1
        
        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            # calculate how many numbers are missing up to arr[mid]
            
            # core logic: in a perfect sequence, with no missing number, value at index mid would be mid+1
            # if numbers are missing then arr[mid] > mid + 1
            # the difference between arr[mid] - (mid+1) tells the number of missing numbers
            missing = arr[mid] - (mid+1) # arr[mid] should be mid+1 if no numbers missing
            if missing < k: # not enough missing - look at right side
                left_pointer = mid + 1
            else:
                right_pointer = mid - 1 # too many missing, look at left side

        return left_pointer + k # the k-th missing number is after 'left' real numbers in arr
