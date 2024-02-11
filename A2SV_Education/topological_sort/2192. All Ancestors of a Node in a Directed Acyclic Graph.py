from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree, graph = self.buildGraph(n, edges)

        res = [set() for _ in range(n)]
        queue = deque()

        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                res[nei].add(node)
                res[nei].update(res[node])

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)


        return [sorted(list(nums)) for nums in res]

    def buildGraph(self, n: int, edges: List[List[int]]):
        indegree = {i:0 for i in range(n)}
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        return indegree, graph
