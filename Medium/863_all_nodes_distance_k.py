"""
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""

"""
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]

Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from collections import deque


class Solution:
    def distanceK(self, root: List[TreeNode], target: int, k: int) -> List[int]:

        # Create parent pointer so that we can scale back up, since we start at target
        parent_to_child = {}  # key is child, val is parent

        def dfs(node, parent):
            if not node:
                return
            parent_to_child[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Begin search from Target
        result = []
        seen = {target}
        queue = deque([(target, 0)])  # (node, distance)

        while queue:
            current_node, dist = queue.popleft()
            if dist == k:
                result.append(current_node.val)
            elif dist < k:
                for neighboring_node in (
                    current_node.left,
                    current_node.right,
                    parent_to_child[current_node],
                ):
                    if neighboring_node and neighboring_node not in seen:
                        queue.append((neighboring_node, dist + 1))
                        seen.add(neighboring_node)

        return result
