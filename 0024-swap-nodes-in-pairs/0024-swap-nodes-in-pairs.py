# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_odd = ListNode(0)
        odd_tail = dummy_odd
        dummy_even = ListNode(0)
        even_tail = dummy_even

        cur = head
        count = 1

        while cur:
            if count % 2 == 1:
                odd_tail.next = cur
                odd_tail = odd_tail.next

            else:
                even_tail.next = cur
                even_tail = even_tail.next

            cur = cur.next
            count += 1
        odd_tail.next = None
        even_tail.next = None
    
        odd = dummy_odd.next

        odd = dummy_odd.next
        even = dummy_even.next

        final_dummy = ListNode(0)
        tail = final_dummy 
        while odd and even:
            tail.next = even
            even = even.next
            tail = tail.next
            tail.next = odd
            odd = odd.next
            tail = tail.next
            
        if even:
            tail.next = even
        if odd:
            tail.next = odd
        return final_dummy.next




        
            
                



