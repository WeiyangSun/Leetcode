"""
958. Check Completeness of a Binary Tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes
in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at the last
level h.
"""

"""
Example 1:
Input: root = [1,2,3,4,5,6]
Output: true

Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: root = [1,2,3,4,5,null,7]
Output: false

Explanation: The node with value 7 isn't as far left as possible.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        end_flag = False

        while queue:
            curr_node = queue.popleft()

            if curr_node is None:
                end_flag = True
            else:
                # if we previously saw a gap and now encounter a real node
                # there is an empty spot on the right
                if end_flag:
                    return False

                queue.append(curr_node.left)
                queue.append(curr_node.right)

        return True # if never found a gap, then tree is complete