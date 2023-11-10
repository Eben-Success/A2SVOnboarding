# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, lowerbound, upperbound):
            if not node:
                return True

            if not (lowerbound < node.val < upperbound):
                return False

            left = helper(node.left, lowerbound, node.val)
            right = helper(node.right, node.val, upperbound)
            return left and right

        return helper(root, float("-inf"), float("inf"))
