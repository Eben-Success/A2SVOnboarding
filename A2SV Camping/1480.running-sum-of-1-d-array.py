#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        running_sum = [0] * n
        running_sum[0] = nums[0]
        
        for i in range(n-1):
            running_sum[i+1] = running_sum[i] + nums[i+1] 
            
        return running_sum
# @lc code=end

