# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0
        tail = head

        while tail:
            tail = tail.next
            count += 1

        num = count // k

        dummy = prev = ListNode(0)
        dummy.next = head
        
        while num:
            cur = prev.next
            nxt = cur.next

            for i in range(1, k):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next

            num -= 1
            prev = cur
            
        return dummy.next

