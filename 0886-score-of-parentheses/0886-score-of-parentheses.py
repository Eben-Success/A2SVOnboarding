class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        ans = 0

        for char in s:
            if char == "(":
                stack.append(ans)
                ans = 0
            
            else:
                ans = stack.pop() + max(ans*2, 1)

        return ans
        