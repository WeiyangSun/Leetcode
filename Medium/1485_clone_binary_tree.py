"""
1485. Clone Binary Tree with Random Pointer

A binary tree is given such that each node contains an additional random pointer which could point
to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented
as a pair of [val, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (in the input) where the random pointer points to, or null if it does
not point to any node.

You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy
class is just a clone of Node class with the same attributes and constructors.
"""

"""
Example 1:
Input: root = [[1,null],null,[4,3],[7,0]]
Output: [[1,null],null,[4,3],[7,0]]

Explanation: The original binary tree is [1,null,4,7].
The random pointer of node one is null, so it is represented as [1, null].
The random pointer of node 4 is node 7, so it is represented as [4, 3] where 3 is the index of node 7 in the array representing the tree.
The random pointer of node 7 is node 1, so it is represented as [7, 0] where 0 is the index of node 1 in the array representing the tree.

Example 2:
Input: root = [[1,4],null,[1,0],null,[1,5],[1,5]]
Output: [[1,4],null,[1,0],null,[1,5],[1,5]]

Explanation: The random pointer of a node can be the node itself.

Example 3:
Input: root = [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
Output: [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
"""


class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


from typing import Optional


class Solution:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[Node]:

        mapping = {}  # maps original node to their clone - keeps track

        def dfs(node):
            # Base Case
            if node is None:
                return None

            # if node is already cloned, return clone
            if node in mapping:
                return mapping[node]

            clone = Node(node.val)  # copy value first
            mapping[node] = clone  # record clone before recursing
            # recursively clone left child
            clone.left = dfs(node.left)
            # recursively clone right child
            clone.right = dfs(node.right)
            # recursively clone random pointer
            clone.random = dfs(node.random)

            return clone

        # start DFS from root and return cloned tree's root
        return dfs(root)


class Solution:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:
        def dfs(root, memo={None: None}):
            if root not in memo:
                memo[root] = NodeCopy(root.val)
                memo[root].left, memo[root].right, memo[root].random = (
                    dfs(root.left),
                    dfs(root.right),
                    dfs(root.random),
                )
            return memo[root]

        return dfs(root)
