"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes
of the list from position left to position right, and return the reversed list.
"""

"""
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Left Pointer:
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next  # moves pointer to just before list reversal point

        start = prev.next  # this is the start of the list reversal
        then = start.next  # one after the start of list reversal

        for _ in range(right - left):
            # Step 1: detach 'then' and link 'start' to 'then.next'
            start.next = then.next
            # Step 2: link 'then' to the front
            then.next = prev.next
            # Step 3: move 'then' to 'prev.next'
            prev.next = then
            # Step 4: advance 'then'
            then = start.next

        return dummy.next
