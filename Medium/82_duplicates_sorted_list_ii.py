"""
82. Remove Duplicates From Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving
only distinct numbers from the original list. Return the linked list sorted as well.
"""

"""
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        # Setting up pointers
        prev = dummy
        current = head

        while current:
            if current.next and current.next.val == current.val:
                # Duplicate Value
                duplicate_val = current.val
                # Skipping all nodes that have the same duplicate value
                while current and current.val == duplicate_val:
                    current = current.next
                # Connect previous unique node to next non-duplicate node
                prev.next = current
            else:
                prev = current
                current = current.next

        return dummy.next
