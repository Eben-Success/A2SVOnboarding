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
            
        print(suffix)

        for i in range(n):
            nums[i] = prefix[i] * suffix[i]        
            
        return nums
# @lc code=end


"""
Initialize an array of len == n with 1.
Starting from the second index, we multiply the 
nums in this order.

nums = [1, 2, 3, 4]

prefix = [1, 1, 1, 1]
suffix = [1, 1, 1, 1]

prefix = [1, 1, 2, 6]
suffix = [24, 12, 4, 1]

final = [24, 12, 8, 6]

n = len(nums)
res = [1] * n
prefix = suffix = [1] * n

# find the prefix product by 1 offset
for i in range(1, len(n)):
    prefix[i] = prefix[i-1] * nums[i-1]
    
# find the suffix product by 1 offset
for i in range(n-2, -1, -1):
    suffix[i] = suffix[i+1] * nums[i+1] 

#find the products
for i in range(n):
    res[i] = suffix[i] * prefix[i]
    
return res
"""