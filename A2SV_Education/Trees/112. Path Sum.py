# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node, target):
            if not node:
                return False
            target -= node.val
            if not node.left and not node.right:
                return target == 0

            
            left = self.hasPathSum(node.left, target)
            right = self.hasPathSum(node.right, target)
            return left or right

        if not root:
            return False

        return helper(root, targetSum)
