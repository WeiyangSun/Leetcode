"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any
node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its
value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to
new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None
of the pointers in the new list should point to nodes in the original list.

For example, if there are 2 nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes
x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of
[val, random_index] where:

- val: an integer representing node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point
to any node.

Your code will only be given the head of the original linked list.
"""

"""
Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""

from typing import Optional, Node


class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # First pass to clone nodes and build map
        old_to_new = {None: None}  # this is to help in the 2nd pass when
        # current_pointer.next or current_pointer.random is None at the end of the list
        current_pointer = head
        while current_pointer:
            old_to_new[current_pointer] = Node(current_pointer.val)
            current_pointer = current_pointer.next

        # Second pass to do rewiring of next and random
        current_pointer = head
        while current_pointer:
            clone_node = old_to_new[current_pointer]
            clone_node.next = old_to_new[current_pointer.next]
            clone_node.random = old_to_new[current_pointer.random]
            current_pointer = current_pointer.next

        return old_to_new[head]


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old_to_new = {}
        current_pointer = head
        # Performing first pass - mapping out nodes
        while current_pointer:
            old_to_new[current_pointer] = Node(current_pointer.val)
            current_pointer = current_pointer.next

        # Performing second pass - rewiring connections
        current_pointer = head
        while current_pointer:
            clone_node = old_to_new[current_pointer]
            clone_node.next = old_to_new.get(current_pointer.next)
            clone_node.random = old_to_new.get(current_pointer.random)
            current_pointer = current_pointer.next

        return old_to_new[head]


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old_to_new = {None: None}
        current_pointer = head

        while current_pointer:
            # Creating base node
            if current_pointer not in old_to_new:
                old_to_new[current_pointer] = Node(current_pointer.val)

            clone_node = old_to_new[current_pointer]

            # Getting Next Connections
            if current_pointer.next not in old_to_new:
                if current_pointer.next:
                    old_to_new[current_pointer.next] = Node(current_pointer.next.val)
            clone_node.next = old_to_new[current_pointer.next]

            # Getting Random Connections
            if current_pointer.random not in old_to_new:
                if current_pointer.random:
                    old_to_new[current_pointer.random] = Node(current_pointer.random.val)
            clone_node.random = old_to_new[current_pointer.random]

            current_pointer = current_pointer.next

        return old_to_new[head]
