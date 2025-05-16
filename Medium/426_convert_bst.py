"""
426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecssor and successor
pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the
first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree
node should point to its predecessor, and the right pointer should point to its successor. You should
return the pointer to the smallest element of the linked list.
"""

"""
Example 1
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor
relationship, while the dashed line means the predecessor relationship.

Example 2:
Input: root = [2,1,3]
Output: [1,2,3]
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        def dfs(node):
            if not node:
                return (None, None)

            # visit left sub-tree
            left_head, left_tail = dfs(node.left)

            if left_tail:
                left_tail.right = node  # right = successor
                node.left = left_tail  # left = predecssor

            # visit right sub-tree
            right_head, right_tail = dfs(node.right)
            if right_head:
                node.right = right_head
                right_head.left = node

            head = left_head if left_head else node
            tail = right_tail if right_tail else node

            return (head, tail)

        head, tail = dfs(root)
        # circular looping
        head.left = tail
        tail.right = head
        return head


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left  # prev in list
        self.right = right  # next in list


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        """Convert BST to sorted circular doubly-linked list in-place."""
        if not root:
            return None

        def dfs(node):
            nonlocal last, head
            if not node:
                return
            # Visit left subtree
            dfs(node.left)

            # Thread current node onto the list
            if last:  # *not* the first node
                last.right = node
                node.left = last
            else:  # first node -> smallest -> head
                head = node
            last = node  # move tail forward

            # Visit right subtree
            dfs(node.right)

        head = last = None  # head = smallest, last = running tail
        dfs(root)

        # Make it circular
        head.left = last
        last.right = head
        return head
