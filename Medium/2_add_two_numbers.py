"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.
"""

"""
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Explanation: 342 + 465 = 807

Example 2:
Input: l1 = [0], l2 = [0]
Output = [0]

Explanation: 0 + 0 = 0

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Explanation: 9999999 + 9999 = 10,009,998
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = ''
        num2 = ''
        
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
            
        total = int(num1[::-1]) + int(num2[::-1]) #807
        total_str = str(total)[::-1] #708
        
        dummy = ListNode(0)
        current = dummy
        
        for digit in total_str:
            current.next = ListNode(int(digit))
            current = current.next #moves pointer up
            
        return dummy.next #skip dummy node to get actual linked list

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from current nodes of l1 and l2 if they exist, otherwise use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum of two values and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            return dummy.next