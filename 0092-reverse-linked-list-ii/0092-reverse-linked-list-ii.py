# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        l_prev = dummy
        cur = head
        idx = 0

        while cur and idx < left - 1:
            cur = cur.next
            l_prev = l_prev.next
            idx += 1

        idx = 0
        r_prev = None
        while cur and idx < right - left + 1:
            nxt = cur.next
            cur.next = r_prev
            r_prev = cur
            cur = nxt
            idx += 1

        l_prev.next.next = cur
        l_prev.next = r_prev

        return dummy.next


        