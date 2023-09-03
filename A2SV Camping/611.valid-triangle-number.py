#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        count = 0
        nums.sort()
        n = len(nums)
        
        for i in range(2, n):
            left = 0
            right = i - 1
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                    
                else:
                    left += 1
                    
        return count
        
# @lc code=end
