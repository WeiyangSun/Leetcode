"""
207. Course Schedule

There are a total of `numCourses` courses you have to take, labelled from `0` to
`numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]`
indicates that you must take course `b_i` first if you want to take course `a_i`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course
`1`.

Return `true` if you can finish all courses. Otherwise, return `false`. 
"""

"""
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false

Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have
finished course 1. So it is impossible.
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_graph = defaultdict(
            list
        )  # list of courses that unlock after pre-requisite cleared
        incoming_deg = [0] * numCourses  # tracks how many prerequisites still missing

        for nxt, prev in prerequisites:
            prerequisites_graph[prev].append(nxt)
            incoming_deg[nxt] += 1  # counting the number of incoming arrows using idx

        queue = deque(
            [ix for ix, val in enumerate(incoming_deg) if val == 0]
        )  # available course to take immediately
        courses_completed = 0

        while queue:
            current_course = queue.popleft()
            courses_completed += 1
            for unlocked_course in prerequisites_graph[current_course]:
                incoming_deg[unlocked_course] -= 1  # erasing incoming arrow
                if incoming_deg[unlocked_course] == 0:  # cleared all pre-requisities
                    queue.append(unlocked_course)  # can now take it freely

        return courses_completed == numCourses
