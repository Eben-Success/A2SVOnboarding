# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = tail = ListNode(float("inf"))
        
        cur = head
        
        while cur:
            if tail.val != cur.val:
                tail.next = cur
                tail = tail.next
            cur = cur.next
            
        tail.next = None
            
        return dummy.next
        
        
        