#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K


# pref[i:j] = pref[j] - pref[i-1]
# pref[j] - pref[i-1] = k
# pref[j] - k = pref[i-1]

# pref[j] - k = 0
# pref[j] = k

# a + b = c
# b - c = a

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cur_sum = 0
        count = 0
        n = len(nums)
        
        hashmap = {0: 1}
        
        for num in nums:
            cur_sum += num
            
            diff = cur_sum - k 
            
            if diff in hashmap:
                count += hashmap[diff]
                
            hashmap[cur_sum] = 1 + hashmap.get(cur_sum, 0)
            
        return count
                
                
        """
        # Intuition
        Let's find the prefix sum of nums
        nums =   [1, 2, 3]
        prefix = [1, 3, 6]
        
        If we want to find the subarrys with 
        
        
        
        1. Create a hashmap and add {0: 1}
        2. Initialize cur_sum, count and n.
        3. Iterate over the nums.
        4. Add nums to cur_sum.
        5. If cu_sum - k in hashmap.
        6. Add to count its value in the hashmap.
        7. Add to the hashmap[cur_sum] with a count of 1
        8. Return count
        """
            
        
# @lc code=end

