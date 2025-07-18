"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked
list.

If there are two middle nodes, return the second middle node.
"""

"""
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]

Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]

Explanation: Since the list has two middle nodes with values 3 and 4, we return
the second one.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next:
            # since fast_pointer is moving 2x speed - when fast_pointer reaches end
            # slow_pointer should hit middle
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer
