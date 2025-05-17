"""
708. Insert into a Sorted Circular Linked List

Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a
value insertVal into the list such that it remains a sorted circular list. The given node can be a reference
to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return
the reference to that single node. Otherwise, you should return the originally given node.
"""

"""
Example 1:
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]

Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference
to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node
1 and node 3. After the insertion, the list should look like this, and we should still return node 3.

Example 2:
Input: head = [], insertVal = 1
Output: [1]

Explanation: The list is empty (given head is null). We create a new single circular list and return the
reference to that single node.

Example 3:
Input: head = [1], insertVal = 0
Output: [1,0]
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> Node:
        new_node = Node(insertVal)

        if not head:
            new_node.next = new_node
            return new_node

        prev_node, current_node = head, head.next
        while True:
            # Scenario A: Found regular spot for insertion between 2 nodes
            if prev_node.val <= new_node.val <= current_node.val:
                break
            # Scenario B: At pivot point where max -> min
            if prev_node.val > current_node.val:
                # Insert if new value is new max or new min
                if new_node.val >= prev_node.val or new_node.val <= current_node.val:
                    break
            # Move forward
            prev_node, current_node = current_node, current_node.next
            # Went around one full loop
            if prev_node == head:
                break

        # Insert new node between previous and current node
        prev_node.next = new_node
        new_node.next = current_node
        return head


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        insert = False
        prev, curr = head, head.next

        while prev:
            if prev.val <= insertVal and insertVal <= curr.val:
                insert = True
            elif prev.val > curr.val:
                if prev.val <= insertVal or curr.val >= insertVal:
                    insert = True
            if insert:
                prev.next = Node(insertVal, curr)
                return head
            prev, curr = curr, curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)

        return head
