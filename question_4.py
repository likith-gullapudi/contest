from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.appendleft(x)
        else:
            self.q2.appendleft(x)

    def pop(self) -> int:
        if self.q1:
            while len(self.q1) > 1:
                self.q2.appendleft(self.q1.pop())
            return self.q1.pop()
        elif self.q2:
            while len(self.q2) > 1:
                self.q1.appendleft(self.q2.pop())
            return self.q2.pop()

    def top(self) -> int:
        if self.q1:
            while len(self.q1) > 1:
                self.q2.appendleft(self.q1.pop())
            temp = self.q1.pop()
            self.q2.appendleft(temp)
            return temp

        elif self.q2:
            while len(self.q2) > 1:
                self.q1.appendleft(self.q2.pop())
            temp = self.q2.pop()
            self.q1.appendleft(temp)
            return temp

    def empty(self) -> bool:
        return (len(self.q1) == 0 and len(self.q2) == 0)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()