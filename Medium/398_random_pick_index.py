"""
398. Random Pick Index

Given an integer array nums with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Implement the Solution class:

- Solution(int[] nums) initializes the object with the array nums.
- int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's,
then each index should have an equal probability of returning.
"""

"""
Example 1:
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
"""

from typing import List
import random

class Solution:
    def __init__(self, nums: List[int]):

        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0 # keep tracks of number of target values seen so far
        chosen_index = -1 # placeholder of index

        for idx, val in enumerate(self.nums):
            if val == target: # found candidate
                count += 1 # update target counts
                
                # pick current index with probability of 1 / count
                if random.randint(1, count) == 1:
                    chosen_index = idx

        return chosen_index


from collections import defaultdict


class Solution:
    def __init__(self, nums: List[int]):

        self.indices = defaultdict(list)
        for idx, val in enumerate(nums):
            self.indices[val].append(idx)

    def pick(self, target: int) -> int:
        bucket = self.indices[target]
        return random.choice(bucket)