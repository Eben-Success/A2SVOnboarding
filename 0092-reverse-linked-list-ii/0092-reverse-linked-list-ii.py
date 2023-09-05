# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        left_prev = dummy
        cur = head
        idx = 0

        while cur and idx < left - 1:
            cur = cur.next
            left_prev = left_prev.next
            idx += 1

        idx = 0
        right_prev = None
        while cur and idx < right - left + 1:
            nxt = cur.next
            cur.next = right_prev
            right_prev = cur
            cur = nxt
            idx += 1

        left_prev.next.next = cur
        left_prev.next = right_prev

        return dummy.next

        



        """
        1. Set dummy node.
        2. Iterate the list to left - 1
        3. Reverse the list to right - left + 1
        4. Reroute head and tail.
        """


        