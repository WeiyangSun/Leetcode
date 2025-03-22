"""
119. Pascal's Triangle II

Given an integer `rowIndex`, return the `rowIndex-th` (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

"""
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        triangle = [[1]]

        for i in range(1, rowIndex+1):

            row = [1]

            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])

            row.append(1)
            triangle.append(row)

        return triangle[-1]


class Solution:
    def getRow(self, rowIndex: int) ->  list[int]:

        row = [1]

        for _ in range(rowIndex):

            newRow = [1]

            for i in range(1, len(row)):
                newRow.append(row[i-1] + row[i])

            newRow.append(1)
            row = newRow

        return row