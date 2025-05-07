"""
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with
val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency
list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the
set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a
reference to the cloned graph.
"""

"""
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]

Explanation: Note that the input contains one empty list. The graph consists of only one
node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []

Explanation: This an empty graph, it does not have any nodes.
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import List, Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional[List[Node]]) -> Optional[List[Node]]:
        if node is None:
            return None

        old_to_new = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            original_currentNode = queue.popleft()
            clone_currentNode = old_to_new[original_currentNode]

            for original_neighbor in original_currentNode.neighbors:
                if original_neighbor not in old_to_new:
                    old_to_new[original_neighbor] = Node(original_neighbor.val)
                    queue.append(original_neighbor)
                clone_currentNode.neighbors.append(old_to_new[original_neighbor])

        return old_to_new[node]

class Solution:
    def cloneGraph(self, node: Optional[List[Node]]) -> Optional[List[Node]]:
        if not node:
            return None

        old_to_new = {}

        def dfs(current_Node):
            if current_Node in old_to_new:
                return old_to_new[current_Node]

            clone_Node = Node(current_Node.val)
            old_to_new[current_Node] = clone_Node

            for neighbor in current_Node.neighbors:
                clone_Node.neighbors.append(dfs(neighbor))
            return clone_Node

        return dfs(node)

