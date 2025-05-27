"""
1522. Diameter of N-Ary Tree

Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path
may or may not pass through the root.

(N-ary Tree input serialization is represented in their level order traversal, each group of children is separated
by the null value.)
"""

"""
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Explanation: Diameter is shown in red color.

Example 2:
Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4

Example 3:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7
"""

from typing import Optional, List


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: "Node") -> int:

        self.max_diameter = 0  # used to track maximum diameter found

        def dfs(node):
            # Base Case
            if not node:
                return 0

            first_max_child, second_max_child = 0, 0

            for child in node.children:
                child_height = dfs(child)

                # update first_max_child and second_max_child
                if child_height > first_max_child:  # current child is the new largest
                    second_max_child = first_max_child  # previous largest becomes second largest
                    first_max_child = child_height  # largest gets updated
                elif child_height > second_max_child:  # current child is the second largest
                    second_max_child = child_height

            # Update global diameter
            self.max_diameter = max(self.max_diameter, first_max_child + second_max_child)
            return (
                first_max_child + 1
            )  # gets the tallest subtree among all the current node's children

        dfs(root)
        return self.max_diameter
