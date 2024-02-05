class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj, indegree = self.buildGraph(graph)
        res = []
        queue = deque()

        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        res.sort()
        return res

    def buildGraph(self, graph):
        n = len(graph)
        adj = defaultdict(list)
        indegree = {i:0 for i in range(n)}

        for i in range(n):
            for val in graph[i]:
                adj[val].append(i)
                indegree[i] += 1
        return adj, indegree
            
        
