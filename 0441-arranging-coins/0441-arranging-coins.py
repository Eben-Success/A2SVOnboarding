class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # maximization problem: low
        
        low, high = 1, n + 1
        
        while low + 1 < high:
            mid = ((high - low) // 2) + low
            
            if self.isArrangeCoins(mid) <= n:
                low = mid
            else:
                high = mid
        return low
    
    def isArrangeCoins(self, num: int) -> int:
        return ((num) * (num + 1)/2)
        