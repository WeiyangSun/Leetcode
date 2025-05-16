"""
210. Course Schedule II

There are a total of numCourses courses you have to take, labelled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisities[i] = [ai, bi] indicates that you must
take course bi, first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid
answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

"""
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]

Explanation: There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]

Explanation: There are a total of 4 courses to take. To take course 3 you should have finished
both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prerequisites_graph = defaultdict(list)
        missing_courses = [0] * numCourses

        for nxt, prev in prerequisites:
            prerequisites_graph[prev].append(nxt)
            missing_courses[nxt] += 1

        courses_completed = []
        queue = deque([ix for ix, val in enumerate(missing_courses) if val == 0])
        while queue:
            current_course = queue.popleft()
            courses_completed.append(current_course)
            for unlocked_courses in prerequisites_graph[current_course]:
                missing_courses[unlocked_courses] -= 1
                if missing_courses[unlocked_courses] == 0:
                    queue.append(unlocked_courses)

        return courses_completed if len(courses_completed) == numCourses else []
