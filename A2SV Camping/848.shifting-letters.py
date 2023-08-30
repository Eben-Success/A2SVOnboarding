#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        shifts.reverse()
        n = len(shifts)
        prefix = [0] * n
        
        prefix[0] = shifts[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] + shifts[i]
        
        prefix.reverse()
        
        res = ""
        
        for i in range(len(s)):
            
            res += chr(ord('a') + (ord(s[i]) - ord('a') + prefix[i]) % 26)     
        return res             
        
        
# @lc code=end

