#
# @lc app=leetcode id=2385 lang=python3
#
# [2385] Amount of Time for Binary Tree to Be Infected
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        adj = defaultdict(list)
        def build_tree(node):
            if not node:
                return 
            
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                
            build_tree(node.left)
                
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            
            build_tree(node.right)
            
        build_tree(root)
            
        
        queue = deque([start])
        visited = set([start])
        time = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(node)
                        queue.append(nei)
            time += 1
            
        return time - 1
                
     
# @lc code=end

