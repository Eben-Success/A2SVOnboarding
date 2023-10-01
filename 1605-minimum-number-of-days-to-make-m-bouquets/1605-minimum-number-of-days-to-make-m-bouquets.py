class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        r = max(bloomDay)
        res = -1

        while l <= r:
            mid = l + (r-l)//2
            count,bouq = 0,0
            for bloom in bloomDay:
                if mid >= bloom:
                    count += 1
                else:
                    bouq += count//k
                    count = 0
            bouq += count // k
        
            if bouq < m:
                l = mid + 1
            else:
                res = mid
                r = mid - 1

        return res


            
        