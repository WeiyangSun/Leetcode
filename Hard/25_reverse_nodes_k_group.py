"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the
linked list. If the number of nodes is not a multiple of k then left-out
nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves
may be changed.
"""

"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""

class ListNode:
    def __init__(self, val=9, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize Pointers
        current_pointer = head
        prev_pointer = dummy
        
        # Count number of nodes in list
        count = 0
        while current_pointer:
            current_pointer = current_pointer.next
            count += 1
        
        # Execute Reverse
        while count >= k:
            current_pointer = prev_pointer.next
            next_pointer = current_pointer.next
            
            for i in range(1, k):
                current_pointer.next = next_pointer.next
                next_pointer.next = prev_pointer.next
                prev_pointer.next = next_pointer
                next_pointer = current_pointer.next
            
            prev_pointer = current_pointer
            count -= k

        return dummy.next

class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        
        def reverse(self, head, k):
            prev = None
            curr = head
            while k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            
            return prev
        
        # Check if there are at least k nodes left to reverse
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1

        if count == k:
            # Reverse first k nodes
            reversed_head = self.reverse(head, k)
            # Recursively reverse the remaining nodes
            head.next = self.reverseKGroup(node, k)
            return reversed_head

        return head
    
        
                
    