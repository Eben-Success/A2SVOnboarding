# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        def build(node):
            if not node:
                return
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
            build(node.left)

            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            build(node.right)
        build(root)

        q = deque([start])
        time = 0
        visit = set()

        while q:
            
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                visit.add(node)
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            time += 1  

        return time-1

            
