#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        left, right = 0, n - 1
        max_area = 0
        
        while left < right:
            diff = right - left
            area = (min(height[left], height[right]) * diff)
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
                
            elif height[left] > height[right]:
                right -= 1
                
            else:
                left += 1
                right -= 1
                
        return max_area
        
# @lc code=end

