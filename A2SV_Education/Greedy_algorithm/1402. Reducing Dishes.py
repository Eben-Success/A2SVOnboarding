class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        res = 0
        
        
        for i in range(n):
            idx = i
            cur = 0
            time = 1
            while idx < n:
                cur += satisfaction[idx] * time
                idx += 1
                time += 1
            res = max(res, cur)
        return res

            """
        [-9, -8, -1, 0, 5]
        [1, 2, 3, 4, 5, 6]

        1. Create a sliding window from 1 to n: time from 1 to n
        2. Slide in n^2 and return the max_sum
        """





        
