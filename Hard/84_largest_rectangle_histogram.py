"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of
each bar is 1, return the area of the largest rectangle in the histogram.
"""

"""
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10

Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Add sentinel height to force stack to empty at the end
        heights.append(0)

        stack = []
        max_area = 0

        for ix, h in enumerate(heights):
            #while current bar is lower than top bar in stack, pop and calculate
            while stack and heights[stack[-1]] > h:
                top_index = stack.pop()
                height_of_bar = heights[top_index]
                
                # if stack is empty width is i
                if not stack:
                    width = ix
                else:
                    width = ix - stack[-1] -1

                # Calculate area
                area = height_of_bar * width
                max_area = max(max_area, area)

            stack.append(ix)

        heights.pop()

        return max_area


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = [-1] #Used for sentinel cases
        n = len(heights)
        max_area = 0

        for i in range(n):
            # pop stack when top of stack >= current height
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height*current_width)
            stack.append(i)

        # Handling remaining bars in stack
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = n - stack[-1] - 1
            max_area = max(max_area, current_height*current_width)
    
        return max_area