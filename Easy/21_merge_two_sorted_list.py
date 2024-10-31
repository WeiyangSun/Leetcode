"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.
"""

"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, lst1 = Optional[ListNode], lst2 = Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        current = dummy

        while lst1 and lst2:
            if lst1.val <= lst2.val:
                current.next = lst1
                lst1 = lst1.next
            else:
                current.next = lst2
                lst2 = lst2.next
            current = current.next
        
        if lst1:
            current.next = lst1
        else:
            current.next = lst2

        return dummy.next