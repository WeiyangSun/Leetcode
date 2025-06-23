"""
1723. Find Minimum Time to Finish All Jobs

You are given an integer array jobs, where jobs[i] is the amount of time it
takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to
exactly one worker. The working time of a worker is the sum of the time it takes
to complete all jobs assigned to them. Your goal is to devise an optimal assignment
such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.
"""

"""
Example 1:
Input: jobs = [3,2,3], k = 3
Output: 3

Explanation: By assigning each person one job, the maximum time is 3.

Example 2:
Input: jobs = [1,2,4,7,8], k = 2
Output: 11

Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.
"""

from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # sort jobs in descneding order to optimize for DFS
        jobs.sort(reverse=True)

        def canBeDone(time_limit):
            # tracker for working time for each worker
            workers = [0] * k

            def dfs(job_index):
                # Base Case
                if job_index == len(jobs): # all jobs assigned
                    return True
                for worker_idx in range(k):
                    if workers[worker_idx] + jobs[job_index] <= time_limit: # if worker can take job
                        workers[worker_idx] += jobs[job_index] # assign job to worker
                        if dfs(job_index + 1): # recurse to next job
                            return True # if found valid assignment
                        workers[worker_idx] -= jobs[job_index] # backtracking
                        # pruning if worker is 0
                        if workers[worker_idx] == 0:
                            break
                return False # no valid assignment for this job

            return dfs(0)

        # Binary Search
        low_limit, high_limit = max(jobs), sum(jobs)
        while low_limit < high_limit:
            mid = (low_limit+high_limit) // 2
            # if possible to assign within mid time
            if canBeDone(mid):
                high_limit = mid # reducing high limit
            else:
                low_limit = mid + 1 # increasing low limit
        return low_limit # the minimum maximum working time