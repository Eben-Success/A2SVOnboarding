from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        graph = self.buildGraph(edges)
        visited = set()

        def dfs(src, dst):
            if src == dst:
                return True
                
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei, dst):
                        return True
                    

        return dfs(source, destination)

    def buildGraph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
        return graph
