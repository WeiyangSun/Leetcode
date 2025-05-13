"""
545. Boundary of Binary Tree

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right,
and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

- The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is
empty.
- If a node is in the left boundary and has a left child, then the left child is in the left boundary.
- If a node is in the left boundary and has no left child, but has a right hild, then the right child is in the left boundary.
- The leftmost leaf is not in the left boundary.

The right boundary is similar to the left boundary, except it is in the right side of the root's right substree. Again,
the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
"""

"""
Example 1:
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]

Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

Example 2:
Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]

Explanation:
- The left boundary follows the path starting from the root's left child 2 -> 4.
  4 is a leaf, so the left boundary is [2].
- The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
  10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
- The leaves from left to right are [4,7,8,9,10].
Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        # Edge Case
        if not root:
            return []

        left_boundary, leaf_order, right_boundary = [], [], []

        # Start from left boundary
        def collect_left(node: Optional[TreeNode], is_boundary: bool):
            if not node:
                return
            if is_boundary and not (node.left is None and node.right is None):
                left_boundary.append(node.val)
            # 2 conditions for it to be considered as a left boundary
            collect_left(node.left, is_boundary)
            collect_left(node.right, is_boundary and not node.left)

        # Do leaf order
        def collect_leaves(node: Optional[TreeNode]):
            if not node:
                return
            if (node.left is None) and (node.right is None):
                leaf_order.append(node.val)
            else:
                collect_leaves(node.left)
                collect_leaves(node.right)

        # End with right boundary
        def collect_right(node: Optional[TreeNode], is_boundary: bool):
            if not node:
                return
            collect_right(node.left, is_boundary and not node.right)
            collect_right(node.right, is_boundary)
            if is_boundary and not (node.left is None and node.right is None):
                right_boundary.append(node.val)

        # Used to handle when only have root node
        if not (root.left is None and root.right is None):
            left_boundary.append(root.val)
        collect_left(root.left, True)
        collect_leaves(root)
        collect_right(root.right, True)

        return left_boundary + leaf_order + right_boundary


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        # Edge Case
        if not root:
            return []

        left_boundary, leaf_order, right_boundary = [], [], []

        # Start from left boundary
        def collect_left(node: Optional[TreeNode], is_boundary: bool):
            if not node:
                return
            if is_boundary and not self._is_leaf(node):
                left_boundary.append(node.val)
            # 2 conditions for it to be considered as a left boundary
            collect_left(node.left, is_boundary)
            collect_left(node.right, is_boundary and not node.left)

        # Do leaf order
        def collect_leaves(node: Optional[TreeNode]):
            if not node:
                return
            if self._is_leaf(node):
                leaf_order.append(node.val)
            else:
                collect_leaves(node.left)
                collect_leaves(node.right)

        # End with right boundary
        def collect_right(node: Optional[TreeNode], is_boundary: bool):
            if not node:
                return
            collect_right(node.left, is_boundary and not node.right)
            collect_right(node.right, is_boundary)
            if is_boundary and not self._is_leaf(node):
                right_boundary.append(node.val)

        # Used to handle when only have root node
        if not self._is_leaf(root):
            left_boundary.append(root.val)
        collect_left(root.left, True)
        collect_leaves(root)
        collect_right(root.right, True)

        return left_boundary + leaf_order + right_boundary

    @staticmethod
    def _is_leaf(node: TreeNode) -> bool:
        return node.left is None and node.right is None
