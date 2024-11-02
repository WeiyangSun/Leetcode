"""
23. Merge k Sorted Lists

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it
"""

"""
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"

def build_linked_list(lst):
    dummy = ListNode(0)
    current = dummy

    for i in lst:
        current.next = ListNode(i)
        current = current.next
    return dummy.next

class Solution:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        flat_dummy = ListNode(0)
        current = flat_dummy
        
        for i in lists:
            linked_list_i = build_linked_list(i)
            while linked_list_i:
                current.next = ListNode(linked_list_i.val)
                current = current.next
                linked_list_i = linked_list_i.next

        values = []
        current = flat_dummy.next
        while current:
            values.append(current.val)
            current = current.next
        
        values.sort()
        output_linked_list = build_linked_list(values)

        return output_linked_list.next

import heapq
class Solution:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        min_heapq = []

        for ix, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(min_heapq, (linked_list.val, ix, linked_list))

        dummy = ListNode(0)
        current = dummy

        while min_heapq:
            val, ix, node = heapq.heappop(min_heapq)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heapq, (node.next.val, ix, node.next))

        return dummy.next

sol = Solution()
print(sol.mergeKLists(lists=[[1,4,5],[1,3,4],[2,6]]))