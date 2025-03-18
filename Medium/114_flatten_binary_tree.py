"""
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the
list and the left child pointer is always null.

- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

"""
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: list[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Flatten left subtree
        self.flatten(root.left)
        # Flatten right subtree
        self.flatten(root.right)

        # Performing Move - store right subtree temporarily
        temp =  root.right
        # Move left subtree to the right
        root.right = root.left
        root.left = None # left pointer must be None in flattened list

        # Traverse to the end of the new right subtree
        current = root
        while current.right:
            current = current.right

        # Attach the old right subtree
        current.right = temp