# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy_lesser = ListNode(-1)
        dummy_greater = ListNode(0)
        tail_less = dummy_lesser
        tail_great = dummy_greater
        cur = head

        while cur:
            if cur.val < x:
                tail_less.next = cur
                tail_less = tail_less.next
            else:
                tail_great.next = cur
                tail_great = tail_great.next
            cur = cur.next

        tail_great.next = None

        tail_less.next = dummy_greater.next

        return dummy_lesser.next

        


        
        