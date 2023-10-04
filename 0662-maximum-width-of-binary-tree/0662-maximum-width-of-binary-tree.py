# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxLevel = 0
        queue = deque([(root, 1)])
        while queue:
            levels = []
            for _ in range(len(queue)):
                node, index = queue.popleft()
                levels.append((node.val, index))

                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right, 2*index + 1))

            if levels:
                maxLevel = max(maxLevel, levels[-1][1] - levels[0][1] + 1)
        return maxLevel

                
        