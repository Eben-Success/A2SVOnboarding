#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        # Time: O(n) | Space: O(n)
        
        count = 0
        n = len(nums)
        cur_sum = 0
        hashmap = {0: 1}
        
        for num in nums:
            cur_sum += num
            
            remainder = cur_sum % k
            
            if remainder in hashmap:
                count += hashmap[remainder]
                
            hashmap[remainder] = 1 + hashmap.get(remainder, 0)
            
        return count
        
# @lc code=end

