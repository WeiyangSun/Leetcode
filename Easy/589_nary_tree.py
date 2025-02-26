"""
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)

Notes: Pre-order means that you will have to go from root all the way down to the 
leaves before moving horizontal to the next node. Depth-First Search. Node -> Left -> Right.
"""

"""
Example 1:
     1
    /|\
   3 2 4
  / \
 5   6

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
        1
    / |  | \
    2 3  4  5
     / \ |  / \
     6 7 8 9  10
       | | |
      11 12 13
       |
      14
    
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Recursive_Solution:
    def preorder(self, root: Node) -> list(int):
        # Store Output Results
        output = []
        self.traverse(root, output)
        return output

    def traverse(self, root: Node, output: list):
        # Base Case: if Root is None
        if root is None:
            return
        # Append value of root node to output
        output.append(root.val)
        # Recursively traverse each node in children array
        for child in root.children:
            self.traverse(child, output)


class Iterative_Solution:
    def preorder(self, root: Node) -> list(int):
        # Base Case: if Root is None
        if root is None:
            return
        q = deque([root])
        output = []

        while q:
            candidate = q.popleft()
            output.append(candidate.val)
            for c in reversed(candidate.children):
                q.appendleft(c)

        return output
