#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        chars = ['a', 'b', 'c', "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        freq = [0] * 26
        
        for c in chars:
            freq[ord(c) - ord('a')] += 1
            
        print(freq)
        
        
        # for num in s:
        #     for i in range(num):
        #         pass
        
# @lc code=end

