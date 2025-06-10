"""
947. Most Stones Removed with Same Row or Column

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have
at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that
has not been removed.

Given an array stones of length n where stones[i] = [x_i, y_i] represents the location of the i-th
stone, return the largest possible number of stones that can be removed.
"""

"""
Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
"""

from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones) # number of stones

        # build adjacency list where each stone index maps to neighbors
        adjacency_graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacency_graph[i].append(j)
                    adjacency_graph[j].append(i)

        # use DFS to count how many clusters exist
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adjacency_graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # for each stone, if it is unvisited, it is a new component - run DFS
        clusters = 0 # count of clusters
        for i in range(n):
            if i not in visited:
                clusters += 1
                dfs(i)

        return n - clusters