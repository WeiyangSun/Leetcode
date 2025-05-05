"""
399. Evaluate Division

You are given an array of variables pairs `equations` and an array of real numbers `values`,
where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`.
Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some queries, where `queries[j] = [Cj, Dj]` represents the `j-th` query where
you must find the answer for `Cj / Dj = ?`.

Return the answers to all queries. If a single answer cannot be determined, return `-1.0`.

Note: The input is always valid. You may assume that evaluating the queries will not result
in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer
cannot be determined for them.
"""

"""
Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5],
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""

from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        #1. Build bidirectional graph
        graph = defaultdict(list)
        for (start, end), value in zip(equations, values):
            graph[start].append((end, value)) # start -> end
            graph[end].append((start, 1/value)) # end -> start

        #2. DFS
        def dfs(src: str, dst: str, product: float, seen: set) -> float:
            if src == dst:
                return product
            seen.add(src)
            for nxt, val in graph[src]:
                if nxt not in seen:
                    res = dfs(nxt, dst, product*val, seen)
                    if res != -1.0:
                        return res
            return -1.0

        #3. Run Workflow
        ans = []
        for x, y in queries:
            if x not in graph or y not in graph:
                ans.append(-1.0)
            elif x == y:
                ans.append(1.0)
            else:
                ans.append(dfs(x, y, 1.0, set()))
        return ans