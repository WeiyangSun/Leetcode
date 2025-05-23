"""
1944. Number of Visible People in a Queue

There are n people standing in a queue, and they numbered from 0 to n-1 in left to right order. You are
given an array heights of distinct integers where heights[i] represents the height of the i-th person.

A person can see another person to their right in the queue if everybody in between is shorter than both
of them. More formally, the i-th person can see the j-th person if i < j and min(heights[i], heights[j])
> max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the i-th person can see to their
right in the queue.
"""

"""
Example 1:
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]

Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.

Example 2:
Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
"""

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # holds heights of people to the right always in strictly decreasing order
        stack = []
        result = []

        # starting from right to left
        for i in range(len(heights) - 1, -1, -1):
            count_visible = 0  # how many people the current person is able to see

            # Pop and count every shorter person - we can see each one
            while stack and heights[i] > stack[-1]:
                stack.pop()  # removes the smaller intermediate hills
                count_visible += 1

            if stack:  # if someone is left in the stack, they must be >= current height
                count_visible += 1  # that person may block the view but is still visible

            result[i] = count_visible  # saves total for this person
            stack.append(heights[i])

        return result
