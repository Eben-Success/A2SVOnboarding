#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        closing = {"}" : "{", ")" : "(", "]" :"[" }
        stack = []
        
        for char in s:
            if char in closing:
                if stack and stack[-1] == closing[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return len(stack) == 0
        
# @lc code=end

