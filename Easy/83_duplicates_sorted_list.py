"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element
appears only once. Return the linked list sorted as well.
"""

"""
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:

        current = head

        while current and current.next:
            # Encountering Duplicate Scenario
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
