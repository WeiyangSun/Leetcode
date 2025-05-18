"""
339. Nested List Weight Sum

You are given a nested list of integers nestedList. Each element is either an integer or a list
whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list
[1, [2,2], [[3], 2], 1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.
"""

"""
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10

Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: 27

Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

Example 3:
Input: nestedList = [0]
Output: 0
"""

from typing import List


class Solution:
    def depthSum(self, nestedList: List["NestedInteger"]) -> int:
        total_sum = 0
        stack = [(element, 1) for element in nestedList]

        while stack:
            current_item, depth = stack.popleft()
            if current_item.isInteger():
                total_sum += current_item.getInteger() * depth
            else:
                for new_element in current_item:
                    stack.append((new_element, depth + 1))

        return total_sum


class Solution:
    def depthSum(self, nestedList: List["NestedInteger"]) -> int:

        self.total_sum = 0

        def dfs(current_list, current_depth):
            if not current_list:
                return

            for element in current_list:
                if element.isInteger():
                    self.total_sum += element.getInteger() * current_depth
                else:
                    dfs(element.getList(), current_depth + 1)

        dfs(nestedList, 1)
        return self.total_sum
