class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # low starts from one not zero
        low, high = 1, max(piles)
        res = 0
        
        while low <= high:
            mid = ((high - low)//2) + low
            
            cur_rate = 0
            
            for num in piles:
                cur_rate += math.ceil(num/mid)
                
            if cur_rate <= h:
                res = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return res
                
        
