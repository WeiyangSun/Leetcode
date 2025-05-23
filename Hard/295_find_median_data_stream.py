"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2+3)/2 = 2.5.

Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10**-5 of the actual answer will be
accepted.
"""

"""
Example 1:
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.low = []  # max-heap for the lower half - stores smaller half with the biggest on top
        self.high = []  # min-heap for the upper half - stores larger half with the smallest on top

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)  # convert to max heap by pushing negative nums
        heapq.heappush(self.high, -heapq.heappop(self.low))  # move largest of low to high
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))  # rebalancing

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):  # left side has one more extra
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
