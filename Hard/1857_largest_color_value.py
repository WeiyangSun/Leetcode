"""
1857. Largest Color Value in a Directed Graph

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n-1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the
i-th node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [a_j, b_j] indicates
that there is a directed edge from node a_j to node b_j.

A valid path in the graph is a sequence of nodes x_1 -> x_2 -> x_3 -> ... -> x_k such that there is a directed
edge from x_i to x_i+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the
most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle. 
"""

"""
Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3

Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:
Input: colors = "a", edges = [[0,0]]
Output: -1

Explanation: There is a cycle from 0 to 0.
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        incoming_edges = [0] * n
        graph = defaultdict(list)

        # initializing graph and incoming_edges for each node
        for in_node, out_node in edges:
            graph[in_node].append(out_node)
            incoming_edges[out_node] += 1

        # initialize memory table for color counts
        color_count = [[0] * 26 for _ in range(n)]
        queue = deque()
        # putting nodes with 0 incoming edges
        for i in range(n):
            if incoming_edges[i] == 0:
                queue.append(i)
            color_count[i][ord(colors[i]) - ord("a")] = 1

        nodes_processed = 0
        max_color_value = 0
        while queue:
            node = queue.popleft()
            nodes_processed += 1

            # Propagate color counts to neighbors
            for neighbor in graph[node]:
                for c in range(26):
                    add = 1 if c == (ord(colors[neighbor]) - ord("a")) else 0
                    color_count[neighbor][c] = max(
                        color_count[neighbor][c], color_count[node][c] + add
                    )
                incoming_edges[neighbor] -= 1
                if incoming_edges[neighbor] == 0:
                    queue.append(neighbor)

            max_color_value = max(max_color_value, max(color_count[node]))

        if nodes_processed < n:
            return -1
        return max_color_value
