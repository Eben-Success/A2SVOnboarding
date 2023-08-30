#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        
        for idx, num in enumerate(nums):
            diff = num - target
            
            if diff in hmap:
                return [idx, hmap[diff]]
            hmap[num] = idx
        
# @lc code=end

