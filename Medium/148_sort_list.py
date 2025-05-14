"""
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order
"""

"""
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List


class Solution:
    @staticmethod
    def merge(list_1, list_2):
        dummy = tail = Node()
        while list_1 and list_2:
            if list_1.val < list_2.val:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next
            tail = tail.next
        tail.next = list_1 or list_2
        return dummy.next

    def sortList(self, head: List[Node]) -> List[Node]:
        # Base Case
        if not head or not head.next:
            return head

        slow_pointer, fast_pointer = head, head.next
        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
        mid_pointer = slow_pointer.next
        slow_pointer.next = None

        left_list = self.sortList(head)
        right_list = self.sortList(mid_pointer)

        return Solution.merge(left_list, right_list)
