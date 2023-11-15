class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]
        heapify(heap)
        while len(heap) > 1:
            num1 = - heappop(heap)
            num2 = - heappop(heap)
            heappush(heap, - (num1 - num2))
        
        return abs(heap[0]) if heap else 0
