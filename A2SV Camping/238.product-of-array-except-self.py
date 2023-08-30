#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(n):
            nums[i] = prefix[i] * suffix[i]        
            
        return nums
# @lc code=end

