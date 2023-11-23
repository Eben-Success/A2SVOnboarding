from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for edge in edges:
            a, b = edge

            graph[a].append(b)
            if len(graph[a]) > 1:
                return a

            graph[b].append(a)
            if len(graph[b]) > 1:
                return b

        """
        center: 2: [1, 4, 3]
        but others:
        1: [2]
        4: [2]
        3: [2]
        """
