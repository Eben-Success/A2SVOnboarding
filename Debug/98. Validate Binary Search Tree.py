"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:

    def ValidateBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, lower_bound, upper_bound):
            if not node:
                return True
            
            if not (node.val > lower_bound and node.val < upper_bound):
                return False
            
            return helper(node.left, lower_bound, node.val) and helper(node.right, node.val, upper_bound)
        
        return helper(root, float("-inf"), float("inf"))


