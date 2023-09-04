# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        nxt_val = node.next.val
        nxt_pointer = node.next.next

        node.val = nxt_val
        node.next = nxt_pointer

        node = node.next
        
