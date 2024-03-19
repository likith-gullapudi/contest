class MyQueue:

    def __init__(self):
        self.a = []  
        self.b = []  

    def push(self, x: int) -> None:
        if self.b == []:
            self.a, self.b = self.b, self.a
        if self.a == []:
            while self.b:
                self.a.append(self.b.pop(-1))
            self.a.append(x)
            while self.a:
                self.b.append(self.a.pop(-1))

    def pop(self) -> int:
        if self.b == []:
            self.a, self.b = self.b, self.a
        return self.b.pop(-1)

    def peek(self) -> int:
        if self.b == []:
            self.a, self.b = self.b, self.a

        return self.b[-1]

    def empty(self) -> bool:
        return self.a == [] and self.b == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
