# First Solution

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res = [[]]
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        for i in range(len(res)):
            val_sum = sum(res[i])
            len_sum = len(res[i])

            res[i] = (val_sum / len_sum)

        return res

# Second solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque([root])

        while queue:
            level_order = []
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                level_order.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sum, level_len = sum(level_order), len(level_order)
            res.append(level_sum / level_len)

        return res
