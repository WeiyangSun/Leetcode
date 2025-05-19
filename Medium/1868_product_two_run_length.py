"""
1868. Product of Two Run-Length Encoded Arrays

Run-length encoding is a compression algorithm that allows for an integer array nums with many segments
of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each
encoded[i] = [val_i, freq_i] describes the i-th segment of repeated numbers in nums where val_i is the
value that is repeated freq_i times.

- For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]].
Another way to read this is "three 1's followed by five 2's".

The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following
steps:

1. Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
2. Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i]*nums2[i].
3. Compress prodNums into a run-length encoded array and return it.

You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2
respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [val_i, freq_i] describes the
i-th segment of nums1, and each encoded2[j] = [val_j, freq_j] describes the j-th segment of nums2.

Return the product of encoded1 and encoded2.

Note: Compression should be done such that the run-length encoded array has the minimum possible length.
"""

"""
Example 1:
Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
Output: [[6,6]]

Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].

Example 2:
Input: encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]
Output: [[2,3],[6,1],[9,2]]

Explanation: encoded1 expands to [1,1,1,2,3,3] and encoded2 expands to [2,2,2,3,3,3].
prodNums = [2,2,2,6,9,9], which is compressed into the run-length encoded array [[2,3],[6,1],[9,2]].
"""

from typing import List


class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        firstEncoder_pointer = 0
        secondEncoder_pointer = 0
        n1 = len(encoded1)
        n2 = len(encoded2)
        result = []

        while firstEncoder_pointer < n1 and secondEncoder_pointer < n2:
            first_val, first_freq = encoded1[firstEncoder_pointer]
            second_val, second_freq = encoded2[secondEncoder_pointer]

            min_overlapping_freq = min(first_freq, second_freq)
            product = first_val * second_val

            # Merge with previous results if same value
            if result and result[-1][0] == product:
                result[-1][-1] += min_overlapping_freq
            else:
                result.append([product, min_overlapping_freq])

            encoded1[firstEncoder_pointer][1] -= min_overlapping_freq
            encoded2[secondEncoder_pointer][1] -= min_overlapping_freq

            if encoded1[firstEncoder_pointer][1] == 0:
                firstEncoder_pointer += 1
            if encoded2[secondEncoder_pointer][1] == 0:
                secondEncoder_pointer += 1

        return result
