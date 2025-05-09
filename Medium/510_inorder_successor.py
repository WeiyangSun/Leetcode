"""
510. Inorder Successor in BST II

Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the
definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
"""

"""
Example 1:
Input: tree = [2,1,3], node = 1
Output: 2

Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.

Example 2:
Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null

Explanation: There is no in-order successor of the current node, so the answer is null.
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

from typing import Optional

class Solution:
    def inorderSuccessor(self, node: Node) -> Optional[Node]:
        # Node has a right child
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            return successor

        # No right child, walk up to find parent where node is a left child
        current_node = node
        while current_node.parent and current_node == current_node.parent.right:
            current_node = current_node.parent
        return current_node.parent