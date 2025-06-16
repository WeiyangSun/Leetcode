"""
621. Task Scheduler

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n.
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in
any order, but there's a constraint: there has to be a gap of at least n intervals between
two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
"""

"""
Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again.
The same applies to task B. In the 3rd interval, neither A nor B can be done,
so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals.
This leads to idling twice between repetitions of these tasks.
"""

from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many times each task appears
        freq_count = Counter(tasks)  # {A: 3, B: 2}
        # Find the max frequency (height of tallest stack - bottleneck)
        max_freq = max(freq_count.values())
        # Finding how many different tasks are tied for max frequency
        max_count = sum(1 for v in freq_count.values() if v == max_freq)
        # Compute ideal length if we lay out only the full rows of tallest stack
        full_sequence_length = (max_freq - 1) * (
            n + 1
        )  # max_freq - 1 because last bunch do not need a trailing gap
        # Add final sequence that contains the same amount of tasks that has max frequency
        # Logic Check: AAABBB with n = 2 -> A _ _ A _ _ AB _ _ B _ _ B overlay → 8
        padded_sequence_length = (
            full_sequence_length + max_count
        )  # max_count accounts for the overhang at the end
        # all other tasks can be filled into the idle slots
        return max(len(tasks), padded_sequence_length)
