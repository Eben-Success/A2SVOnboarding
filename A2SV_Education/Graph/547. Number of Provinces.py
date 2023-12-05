class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = set()
        count = 0

        adj = {i+1:[] for i in range(n)}
        visited = set()
        for i in range(n):
            for j in range(n):
                if i+1 != j+1:
                    if isConnected[i][j] == 1:
                        adj[i+1].append(j+1)

        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
                        
        
        for key in adj.keys():
            if key not in visited:
                dfs(key)
                count += 1
        return count
