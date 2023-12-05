from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(dislikes)
        color = [-1 for _ in range(n+1)]

        def dfs(node, graph):
            res = True
            for nei in graph[node]:
                if color[nei] == -1:
                    if color[node] == 0:
                        color[nei] = 1
                    else:
                        color[nei] = 0
                    res = res and dfs(nei, graph)
                else:
                    res = res and color[nei] != color[node]
            return res

        res = True
        for node in graph.keys():
            if color[node] == -1:
                color[node] = 0
                res = res and dfs(node, graph)
        return res
        

    def buildGraph(self, edges):
        graph = defaultdict(list)

        for edge in edges:
            a , b = edge
            graph[a].append(b)
            graph[b].append(a)
        return graph
