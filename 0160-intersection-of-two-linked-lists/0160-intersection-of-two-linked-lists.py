# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None
        
        cur1 = headA
        cur2 = headB
        
        while cur1 != cur2:
            
    
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
            
            
        return cur1