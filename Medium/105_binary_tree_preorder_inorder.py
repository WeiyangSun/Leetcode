"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and
return the binary tree.
"""

"""
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> [TreeNode]:

        if not preorder or not inorder:
            return None

        # Building Root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Finding position of root in inorder
        root_idx_inorder = inorder.index(root_val)
        # Elements left of root - left subtree
        left_tree_inorder = inorder[:root_idx_inorder]
        # Elements right of root - right subtree
        right_tree_inorder = inorder[root_idx_inorder + 1 :]

        # Size of Left Subtree
        left_tree_size = len(left_tree_inorder)

        # Switching to Preorder
        left_tree_preorder = preorder[1 : left_tree_size + 1]
        right_tree_preorder = preorder[left_tree_size + 1 :]

        root.left = self.buildTree(left_tree_preorder, left_tree_inorder)
        root.right = self.buildTree(right_tree_preorder, right_tree_inorder)

        return root


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> [TreeNode]:

        # Base Case
        if not preorder or not inorder:
            return None

        inorder_map = {v: ix for ix, v in enumerate(inorder)}

        def helper(preorder_left, preorder_right, inorder_left, inorder_right):

            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None

            # Building Root Value
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)
            root_idx = inorder_map[root_val]

            left_subtree_size = root_idx - inorder_left

            # Recursively build left subtree
            root.left = helper(
                preorder_left + 1, preorder_left + left_subtree_size, inorder_left, root_idx - 1
            )
            # Recursively build right subtree
            root.right = helper(
                preorder_left + 1 + left_subtree_size, preorder_right, root_idx + 1, inorder_right
            )

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
