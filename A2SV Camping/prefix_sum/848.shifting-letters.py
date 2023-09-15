#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start

import string

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        n = len(shifts)
        
        alphabets = list(string.ascii_lowercase)
        
        suffix = [0] * n
        suffix[-1] = shifts[-1]
        
        idx = n - 2
        
        while idx > -1:
            suffix[idx] = suffix[idx + 1] + shifts[idx]
            idx -= 1
        
        res = ""
        
        for i in range(len(s)):
            
            # res += chr(ord('a') + (ord(s[i]) - ord('a') + suffix[i]) % 26)     
            
            char_idx = alphabets.index(s[i])
            res += alphabets[(char_idx + suffix[i]) % 26]
        return res             
        
        
# @lc code=end

