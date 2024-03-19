class MyQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []  

    def push(self, x: int) -> None:
        if self.queue2 == []:
            self.queue1, self.queue2 = self.queue2, self.queue1
        if self.queue1 == []:
            while self.queue2:
                self.queue1.append(self.queue2.pop(-1))
            self.queue1.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.pop(-1))

    def pop(self) -> int:
        if self.queue2 == []:
            self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop(-1)

    def peek(self) -> int:
        if self.queue2 == []:
            self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2[-1]

    def empty(self) -> bool:
        return self.queue1 == [] and self.queue2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
