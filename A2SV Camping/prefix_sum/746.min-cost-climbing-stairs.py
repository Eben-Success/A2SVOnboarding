#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# Naive Time: O(2^n) -> O(n)
# Space: O(n)

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #[0, 0, 0, 0]
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            # cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])  #OR       
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])
            
        
# @lc code=end

