#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

"""
If the sum of gas < sum of cost: it's not possible so
return -1

Get the difference between the gas and cost.
Add diff to total.
If total < 0:
reset total
reset start to i + 1
return start

"""

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        start = 0
        
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            total += gas[i] -
            cost[i]
            
            if total < 0:
                total = 0
                start = i + 1
                
        return start
        
# @lc code=end

