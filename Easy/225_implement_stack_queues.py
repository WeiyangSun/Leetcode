"""
225. Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack
(push, top, pop, and empty).

Implement the MyStack class:

- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

You must use only standard operations of a queue, which means that only push
to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may
simulate a queue using a list or deque (double-ended queue) as long as you use
only a queue's standard operations.
"""

"""
Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.queue1 = deque()  # this holds stack elements
        self.queue2 = deque()  # this is for handling push operations

    def push(self, x: int) -> None:
        self.queue2.append(x)  # add new element to queue2
        while self.queue1:
            self.queue2.append(
                self.queue1.popleft()
            )  # remove element from queue1 and append to queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1
