"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adj = {}
        for emp in employees:
            adj[emp.id] = emp

        total = 0
        def dfs(node):
            nonlocal total

            if not node:
                return

            total += node.importance
            for id in node.subordinates:
                dfs(adj[id])
        
        dfs(adj[id])
        return total
