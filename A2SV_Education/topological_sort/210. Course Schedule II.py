class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegree = self.buildGraph(numCourses, prerequisites)

        res = []
        queue = deque()
        for course in indegree:
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return res if len(res) == numCourses else []

    def buildGraph(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(numCourses):
            indegree[i] = 0

        for pre in prerequisites:
            u, v = pre
            graph[v].append(u)
            indegree[u] += 1

        return graph, indegree
        
