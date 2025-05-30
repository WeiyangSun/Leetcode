"""
86. Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before
nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""

"""
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: list[ListNode], x: int) -> list[ListNode]:

        # Create 2 empty list
        dummy_lesser = ListNode(0)
        dummy_greater = ListNode(0)
        # Create 2 pointers
        lesser = dummy_lesser
        greater = dummy_greater

        # Create 3rd pointer for head
        current = head

        while current:
            if current.val < x:
                lesser.next = current
                lesser = lesser.next
            else:
                greater.next = current
                greater = greater.next

            current = current.next

        # Join 2 list together
        greater.next = None  # End greater list
        lesser.next = dummy_greater.next

        return dummy_lesser.next
