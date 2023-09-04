#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        n = len(tokens)
        left, right = 0, n - 1
        cur_score = 0
        max_score = 0
        
        while left <= right:
            if power >= tokens[left]:
                cur_score += 1
                power -= tokens[left]
                left += 1
                max_score = max(max_score, cur_score)
                
            elif cur_score > 0:
                if power < tokens[right]:
                    power += tokens[right]
                    cur_score -= 1
                    right -= 1
                    
            else: 
                break
        
        return max_score
          
# @lc code=end

