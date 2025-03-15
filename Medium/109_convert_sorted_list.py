"""
109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
height-balanced binary search tree.
"""

"""
Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: list[ListNode]) -> [TreeNode]:

        def findMiddleNode(start):
            prev = None
            slow = start
            fast = start

            # Move slow pointer by 1 and fast pointer by 2
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:  # If prev is not None
                prev.next = None

            return slow

        # Base Case
        if not head:
            return None
        if not head.next:  # only has 1 value
            return TreeNode(head.val)

        mid = findMiddleNode(head)

        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
