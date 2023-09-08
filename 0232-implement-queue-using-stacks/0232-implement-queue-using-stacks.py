class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []
        

    def push(self, x: int) -> None:
        if self.stack:
            while len(self.stack) > 0:
                self.temp.append(self.stack.pop())

        self.stack.append(x)
        if self.temp:
            while len(self.temp) > 0:
                self.stack.append(self.temp.pop())

        print(self.stack)
        

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()