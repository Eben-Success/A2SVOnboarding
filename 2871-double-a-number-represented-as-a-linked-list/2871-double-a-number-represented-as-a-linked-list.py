# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        9 -> 9 -> 9
        """
        
        dummy = ListNode(0)
        tail = dummy
        head1 = self.reverseList(head)
        cur = head1
        carry = 0

        while cur:
            val = (cur.val * 2) + carry
            num = val % 10
            carry = val // 10

            newNode = ListNode(num)
            tail.next = newNode
            tail = tail.next
            cur = cur.next

        if carry:
            newNode = ListNode(carry)
            tail.next = newNode

        return self.reverseList(dummy.next)
   

    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = node

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
