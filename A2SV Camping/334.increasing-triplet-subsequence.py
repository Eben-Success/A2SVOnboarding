#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        
        for num in nums:
            if num <= first_num:
                first_num = num
                
            elif num <= second_num: 
                second_num = num
            
            else:
                return True
            
        return False
        
# @lc code=end

