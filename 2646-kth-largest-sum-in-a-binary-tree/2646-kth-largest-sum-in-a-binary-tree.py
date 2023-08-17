# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 0

        queue = deque([root])
        res = []

        while queue:
            n = len(queue)
            level_sum = 0
            for _ in range(n):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_sum)

        res = [-num for num in res]

        if k > len(res):
            return - 1

        heapq.heapify(res)

        while k > 0:
            num = - heapq.heappop(res)
            k -= 1

        return num
