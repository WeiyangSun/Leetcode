"""
11. Container with Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two
endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most
water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

"""
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:

            width = right - left
            area = width * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class Solution:
    def maxArea(self, height: list[int]) -> int:

        memo = {}
        n = len(height)

        def helper(left: int, right: int) -> int:
            if left >= right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            current_area = (right - left) * min(height[left], height[right])
            area_move_left = helper(left + 1, right)
            area_move_right = helper(left, right - 1)

            memo[(left, right)] = max(current_area, area_move_left, area_move_right)

            return memo[(left, right)]

        return helper(0, n - 1)


sol = Solution()
print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
