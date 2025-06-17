"""
2616. Minimize the Maximum Difference of Pairs

You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of
nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no
index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is
|nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty
set to be zero.
"""

"""
Example 1:
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1

Explanation: The first pair is formed from the indices 1 and 4, and the second pair
is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1.
Therefore, we return 1.

Example 2:
Input: nums = [4,2,1,2], p = 1
Output: 0

Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is
|2 - 2| = 0, which is the minimum we can attain.
"""

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        # can we form at least p pairs if the max allowed gap is max_diff
        def can_make_pairs(max_diff: int) -> bool:
            pair_count = 0
            i = 0  # pointer along sorted list
            n = len(nums)

            while i < n - 1:
                # try to pair nums[i] with nums[i+1] if gap is <= max_diff
                if nums[i + 1] - nums[i] <= max_diff:
                    pair_count += 1  # we make a pair
                    i += 2  # skip the pair
                else:
                    i += 1  # move on and try next num

            return pair_count >= p

        low_diff, high_diff = 0, nums[-1] - nums[0]  # this is the max gap
        result = 0

        while low_diff <= high_diff:
            mid_diff = (low_diff + high_diff) // 2
            if can_make_pairs(mid_diff):
                result = mid_diff
                high_diff = mid_diff - 1
            else:
                low_diff = mid_diff + 1

        return result
