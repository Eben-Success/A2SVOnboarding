class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_num = max(piles) # O(n)
        
        left, right = 1, max_num

        while left < right:
            mid = ((right - left) // 2) + left
            sum_ = 0
            for pile in piles:
                sum_ += math.ceil(pile/mid)
                
            
            if sum_ <= h:
                right = mid

            else:
                left = mid + 1

        return left


        