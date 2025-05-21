"""
2071. Maximum Number of Tasks You Can Assign

You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed
integer array tasks, with the i-th task requiring tasks[i] strength to complete. The strength
of each worker is stored in a 0-indexed integer array workers, with the j-th worker having
workers[j] strength. Each worker can only be assigned to a single task and must have a strength
greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength.
You can decide which workers receive the magical pills, however, you may only give each worker
at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength,
return the maximum number of tasks that can be completed.
"""

"""
Example 1:
Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3

Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)

Example 2:
Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1

Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)

Example 3:
Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2

Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.
"""

from typing import List
from collections import deque


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:

        # Pre-sorting for two-pointer convenience
        tasks.sort()  # lightest to heaviest
        workers.sort()  # weakest to strongest

        def able_to_handle(no_of_tasks):
            remaining_pills = pills
            worker_queue = deque() # reserved workers for possibility of improved strength
            worker_idx = len(workers - 1) # index of the strongest unused worker

            # Iterate tasks from heaviest to lighest among the no_of_tasks lightest tasks
            for individual_task in reversed(tasks[:no_of_tasks]):
                # Case 1: if there is a queue of reserved workers, pick the oldest
                if worker_queue and worker_queue[0] >= individual_task:
                    worker_queue.popleft()
                # Case 2: use a fresh, strongest work without a pill
                elif worker_idx >= 0 and workers[worker_idx] >= individual_task:
                    worker_idx -= 1
                # Case 3: Must use a pill
                else:
                    # putting all workers who after taking the pill can do the task into reserve
                    while worker_idx >= 0 and workers[worker_idx] + strength >= individual_task:
                        worker_queue.append(workers[worker_idx]) # put worker into reserve slot first
                        worker_idx -= 1
                    # No more reserved workers and all pills are used up
                    if not worker_queue or remaining_pills == 0:
                        return False
                    # Use the weakest of reserved candidates with a pill
                    worker_queue.pop()
                    remaining_pills -= 1
            return True

        low_pointer, high_pointer = 0, min(len(tasks), len(workers))
        while low_pointer < high_pointer:
            # mid_pointer represents the number of tasks we are currently trying to assign
            mid_pointer = (low_pointer + high_pointer + 1) // 2
            if able_to_handle(mid_pointer):
                low_pointer = mid_pointer
            else:
                high_pointer = mid_pointer - 1

        return low_pointer
