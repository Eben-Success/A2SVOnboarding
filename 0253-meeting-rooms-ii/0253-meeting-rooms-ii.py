class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
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
        