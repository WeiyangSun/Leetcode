"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

- MovingAverage(size: int) initializes the object with the size of the window size.
- Next(val: int) returns the moving average of the last size values of the stream.
"""

"""
Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
"""

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.sum += val
        else:
            self.sum -= self.window.popleft()
            self.queue.append(val)
            self.sum += val
        return self.sum / len(self.window)


class MovingAverage:

    def __init__(self, size: int):

        self.size = size
        self.window = deque()
        self.curr_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.curr_sum += val

        if len(self.window) > self.size:
            self.curr_sum -= self.window.popleft()

        return self.curr_sum / len(self.window)