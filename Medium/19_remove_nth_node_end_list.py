"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head
"""

"""
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:

        dummy = ListNode(0)
        dummy.next = head  # dummy -> list_node -> list_node -> list_node

        first_pointer = dummy
        second_pointer = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            if first_pointer:
                first_pointer = first_pointer.next
            else:
                return head  # if n is larger than the length of the list
        # Move both pointers until first reaches the end
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        second_pointer.next = second_pointer.next.next

        return dummy.next


def create_linked_list_from_list(input: list) -> [ListNode]:

    dummy = ListNode(0)
    current = dummy

    for i in input:
        current.next = ListNode(i)
        current = current.next

    return dummy.next


def create_list_from_linked_list(input: [ListNode]) -> list:

    output_list = []
    current = input

    while current:
        output_list.append(current.value)
        current = current.next

    return output_list
