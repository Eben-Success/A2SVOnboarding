class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or self.min_stack and self.min_stack[-1] >= val:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if self.min_stack and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()