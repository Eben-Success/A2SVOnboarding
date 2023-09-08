class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:
            
            if char == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.add(a, b))

            elif char == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.subtract(a, b))

            elif char == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.multiply(a, b))

            elif char == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.divide(a, b))
            else:
                stack.append(int(char))
        return stack[0]

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return int(a / b)
        