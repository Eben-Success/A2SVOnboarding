class MinStack:

    def __init__(self):
        self.min_elem = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_elem or val <= self.min_elem[-1]:
            self.min_elem.append(val)
        

    def pop(self) -> None:
        if self.min_elem and self.min_elem[-1] == self.stack[-1]:
            self.min_elem.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_elem:
            return self.min_elem[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()