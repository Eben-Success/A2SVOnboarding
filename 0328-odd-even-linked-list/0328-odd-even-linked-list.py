# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_odd = ListNode(0)
        dummy_even = ListNode(0)
        tail_odd = dummy_odd
        tail_even = dummy_even
        cur = head
        count = 1

        while cur:
            if count % 2 == 1:
                tail_odd.next = cur
                tail_odd = tail_odd.next

            else:
                tail_even.next = cur
                tail_even = tail_even.next

            cur = cur.next
            count += 1

        tail_odd.next = dummy_even.next
        tail_even.next = None

        
        return dummy_odd.next