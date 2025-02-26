"""
106. Construct Binary Tree from InOrder and PostOrder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.
"""

"""
Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> [TreeNode]:

        if not inorder or not postorder:
            return None

        # Building Root
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # INORDER
        root_idx_inorder = inorder.index(root_val)
        # Left Tree - InOrder
        left_tree_inorder = inorder[:root_idx_inorder]
        # Right Tree - InOrder
        right_tree_inorder = inorder[root_idx_inorder + 1 :]

        # POSTORDER
        left_tree_size = len(left_tree_inorder)
        # Left Tree - PostOrder
        left_tree_postorder = postorder[:left_tree_size]
        # Right Tree - PostOrder
        right_tree_postorder = postorder[left_tree_size:-1]

        # RECURSIVE
        root.left = self.buildTree(left_tree_inorder, left_tree_postorder)
        root.right = self.buildTree(right_tree_inorder, right_tree_postorder)

        return root


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> [TreeNode]:

        if not inorder or not postorder:
            return None

        # Build Map to get index of a node val in the inorder array
        inorder_map = {v: ix for ix, v in enumerate(inorder)}

        # function will operate on subrange of inorder and postorder
        def helper(inorder_left, inorder_right, postorder_left, postorder_right):
            # if left pointer crosses right pointer - Not Valid
            if inorder_left > inorder_right or postorder_left > postorder_right:
                return None

            # Get Root Value
            root_val = postorder[postorder_right]
            root = TreeNode(root_val)
            root_idx = inorder_map[root_val]

            left_subtree_size = root_idx - inorder_left

            # Recursively build left subtree
            root.left = helper(
                inorder_left, root_idx - 1, postorder_left, postorder_left + left_subtree_size - 1
            )
            # Recursively build right subtree
            root.right = helper(
                root_idx + 1,
                inorder_right,
                postorder_left + left_subtree_size,
                postorder_right - 1,
            )

            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
