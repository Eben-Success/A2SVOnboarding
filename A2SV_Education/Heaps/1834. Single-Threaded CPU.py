class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, num in enumerate(tasks):
            num += [idx]

        tasks.sort(key=lambda x:x[0])

        n = len(tasks)
        res = []
        heap = []

        idx = 0
        t = tasks[0][0]

        while heap or idx < n:
            while idx < n and t >= tasks[idx][0]:
                heapq.heappush(heap, [tasks[idx][1], tasks[idx][2]])
                idx += 1

            if len(heap) == 0:
                t = tasks[idx][0]

            else:
                time, i = heapq.heappop(heap)
                t += time
                res.append(i)

        return res
