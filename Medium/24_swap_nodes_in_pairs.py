"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
"""

"""
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1,2,3]
Output: [2,1,3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, lst: [ListNode]) -> [ListNode]:
        dummy = ListNode(0)
        dummy.next = lst
        current = dummy  # pointer

        while current.next and current.next.next:
            first_node = current.next
            second_node = current.next.next

            # Swapping
            first_node.next = second_node.next  # first node points to third node
            second_node.next = first_node  # second node points to first node
            current.next = second_node

            current = first_node

        return dummy.next
