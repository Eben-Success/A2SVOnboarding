import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        heap = [(nums[0], 1)]
        n = len(nums)

        for i in range(1, n):

            while heap and heap[0][0] <  nums[i] - 1:
                if heap[0][1] < 3:
                    return False
                heapq.heappop(heap)
               
            if heap and (1 + heap[0][0]) == nums[i]:
                num, count = heapq.heappop(heap)
                heapq.heappush(heap, (nums[i], count + 1))
            else:
                heapq.heappush(heap, (nums[i], 1))

        for num in heap:
            if num[1] < 3:
                return False

        return True
