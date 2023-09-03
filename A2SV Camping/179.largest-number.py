#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start

class Comparer(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # convert the nums to string
        nums = [str(num) for num in nums]
        
        # sort by the comparer
        nums.sort(key=Comparer)
        
        # Join the nums
        largest = "".join(nums)
        
        # Edge case: If all are 0s, return 0
        return "0" if largest[0] == "0" else largest
            
# @lc code=end

