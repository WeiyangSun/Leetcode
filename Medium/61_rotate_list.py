"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""

"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        if not head or not head.next or k == 0:
            return head

        length_of_linked_list = 1
        current = head
        while current.next:
            current = current.next
            length_of_linked_list += 1

        old_tail = current

        # Adjusting k % length_of_linked_list == rotating linked_list by k
        k = k % length_of_linked_list
        if k == 0: # Effectively no rotation is needed
            return head

        # Finding the new tail
        steps_to_new_tail = length_of_linked_list - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        old_tail.next = head

        return new_head