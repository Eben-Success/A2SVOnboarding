"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

from typing import List
import heapq

class Solve:
    def minMeetingRoom(intervals: List[int]) -> int:
        
        # length of intervals.
        n = len(intervals)
        
        # keep track of the end times.
        heap = []
        
        # sort by start times.
        intervals.sort(key=lambda x: x[0])
        
        # Push the first interval into the heap.
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, n):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
                
            heapq.heappush(heap, intervals[i][1])
            
        return len(heap)
        
        