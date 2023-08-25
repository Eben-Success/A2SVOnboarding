class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # intervals.sort() # O(nlogn)
        # res = [intervals[0]] # O(n)

        # for start, end in intervals[1:]: # O(n)
        #     if res[-1][1] >= start:
        #         res[-1][1] = max(res[-1][1], end)
        #     else:
        #         res.append([start, end])

        # return res
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            #compare end and start intervals
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                
            else:
                res.append(intervals[i])

        return res
    
