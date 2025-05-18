"""
378. Kth Smallest Element in a Sorted Matrix

Given an nxn matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n**2).
"""

"""
Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13

Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left_pointer, right_pointer = matrix[0][0], matrix[-1][-1]

        def countLessEqual(target):
            row, col = n - 1, 0
            count = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        while left_pointer < right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            count = countLessEqual(mid_pointer)
            if count < k:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer

        return left_pointer
