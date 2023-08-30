#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hmap = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jki", "6" : "mno", "7" : "pqrs", "8":"tuv", "9":"wxyz"}
        
        res = []
        
        if not digits: return res
        
        def backtrack(i, cur):
            if len(cur) == len(digits):
                comb = "".join(cur)
                res.append(comb)
                return res
            
            letters = hmap[digits[i]]
            for letter in letters:
                backtrack(i+1, cur + [letter])
                
        backtrack(0, [])   
        return res       
        
# @lc code=end

